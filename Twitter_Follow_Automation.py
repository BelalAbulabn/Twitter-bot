import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import logging

logging.basicConfig(level=logging.INFO)

class TwitterBot:
    def __init__(self, username, password, input_type, user, hashtag):
        """
        Initialize the webdriver and assign the input parameters to class variables.
        """
        self.username = username
        self.password = password
        self.input_type = input_type
        self.user = user
        self.hashtag = hashtag
        self.webdriver = webdriver.Chrome(executable_path=self.get_chrome_driver_path())

    def get_chrome_driver_path(self):
        """
        Get the chrome driver path
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_dir, "chromedriver")
        return chrome_driver_path

    def login(self):
        """
        Login to twitter using the provided username and password.
        """
        self.webdriver.get('https://twitter.com/login')
        time.sleep(4)

        email_field = self.webdriver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        email_field.clear()
        email_field.send_keys(self.username)
        email_field.send_keys(Keys.RETURN)
        time.sleep(4)

        password_field = self.webdriver.find_element(By.XPATH, '//input[@name="password"]')
        password_field.send_keys(self.password)
        time.sleep(4)
        password_field.send_keys(Keys.RETURN)
        time.sleep(4)

    def get_usernames(self):
        """
        Get a list of usernames from the specified page.
        """
        usernames_detected = self.webdriver.find_elements(By.XPATH, '//a[@role="link" and @aria-hidden="true"]')
        usernames_prelist = [arroba.get_attribute('href') for arroba in usernames_detected]
        return usernames_prelist

    def follow_users(self, usernames_list):
        """
        Follow a specified number of users with a specified cooldown time between follows.
        """
        # Constants
        MAX_FOLLOWS = 20
        COOLDOWN_TIME_MINUTES = 10
        INTERVAL_MIN, INTERVAL_MAX = (6, 18)

        # Counters
        follow_counter = 0
        cooldown_counter = 0
        scroll_counter = 0

        # Lists
        already_followed_users = []
        users_to_follow_list = []

        for k in range(1, 1000):
            if scroll_counter > 0:
                self.webdriver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)
            try:
                usernames_list = self.get_usernames()
                for username in usernames_list:
                    if username not in already_followed_users:
                        users_to_follow_list.append(username)
            except StaleElementReferenceException as e:
                logging.error(e)
                continue

            for username in users_to_follow_list:
                try:
                    follow_button = self.webdriver.find_element(By.XPATH, f'//a[@href="{username}"]/../../div[2]/div[1]/div/div[2]/div[3]/div')
                    follow_button.click()
                    already_followed_users.append(username)
                    follow_counter += 1
                    time.sleep(random.randint(INTERVAL_MIN, INTERVAL_MAX))
                except (NoSuchElementException, StaleElementReferenceException) as e:
                    logging.error(e)
                    continue

                if follow_counter >= MAX_FOLLOWS:
                    follow_counter = 0
                    time.sleep(COOLDOWN_TIME_MINUTES * 60)
                    cooldown_counter += 1

                if cooldown_counter > 0 and follow_counter == 0:
                    self.webdriver.execute_script('window.scrollTo(0,0)')
                    time.sleep(5)
                    scroll_counter += 1
                    users_to_follow_list = []

        self.webdriver.close()

# Get input from user
input_type = input("Select your index (hashtag or username): ")
while input_type != "username" and input_type != "hashtag":
    input_type = input("Wrong command, try again\nSelect your index (hashtag or username): ")

if input_type == "username":
    user = input("Type the username: ")
    hashtag = ""

if input_type == "hashtag":
    hashtag = input("Type the hashtag: ")
    user = ""

username = input("Enter your Twitter username: ")
password = input("Enter your Twitter password: ")

# Initialize and run the bot
bot = TwitterBot(username, password, input_type, user, hashtag)
bot.login()
bot.follow_users()
