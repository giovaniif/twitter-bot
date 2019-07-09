from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name('js-username-field')
        password = bot.find_element_by_class_name('js-password-field')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        self.ask_for_search_term()


    def ask_for_search_term(self):
        search_term = input('What do you want to search for? ')
        self.search_for_tweets(search_term)


    def search_for_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=tyah')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

        self.like_tweets(links)


    def like_tweets(self, links):
        bot = self.bot
        for link in links:
            bot.get('https://twitter.com' + link)
            try:
                bot.find_element_by_class_name('HeartAnimation').click()
                time.sleep(5)
            except Exception as ex:
                time.sleep(60)


def get_parameters_and_init():
    username = input('Username or email: ')
    password = input('Password: ')

    user = TwitterBot(username, password)
    time.sleep(1)
    print("We're trying to log you in...")
    user.login()


get_parameters_and_init()
