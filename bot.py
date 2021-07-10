from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def checkIfLikePresent(self, className):
        i = 0
        bot = self.bot
        while(i < 1):
            if bot.find_elements_by_class_name(className):
                try:
                    like = bot.find_element_by_class_name(className)
                    like.send_keys(Keys.ENTER)
                except Exception as ex:
                    time.sleep(60)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(1)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        time.sleep(1)

    def likeImgChlo(self):
        bot = self.bot
        bot.get('https://twitter.com/bagofpiss/media')
        time.sleep(30)

    def gotoZay(self):
        bot = self.bot
        bot.get('https://twitter.com/zayyuuhh/media')

    def likeImgZay(self):
        bot = self.bot
        if (elem.get_attribute('aria-label') == 'like'):
          like = [elem.get_attribute('aria-label')]
        try:
            like = bot.find_element_by_class_name('')
            like.send_keys(Keys.ENTER)
        except Exception as ex:
            time.sleep(5)

    def saveImg(self):
        bot = self.bot
        bot.get('https://twitter.com/bagofpiss/media')
        time.sleep(30)


ed = TwitterBot('AndrianiPerez', 'A10231016p')
ed.login()
i = 0
while(i < 1):
    ed.gotoZay()
    time.sleep(3)
    ed.likeImgZay()
    #ed.checkIfLikePresent('css-1dbjc4n r-18u37iz r-1h0z5md')
    print("loop starts again")
