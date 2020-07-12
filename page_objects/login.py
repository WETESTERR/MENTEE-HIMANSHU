import time

import pytest
import self
from selenium.webdriver.common.by import By

from config import sleep_time, wait_time
from page_objects.common import Common
from utilities import driver
from utilities.locator_strategy import LocatorStrategy
from utilities.log import Logs


class Login(Common,Logs):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = self.logger()



    login_button = LocatorStrategy.locator_by_xpath("//a[@class='login']")
    email_field = LocatorStrategy.locator_by_id("email")
    password_field = LocatorStrategy.locator_by_id("passwd")
    submit_button = LocatorStrategy.locator_by_name("SubmitLogin")
    logout_button = LocatorStrategy.locator_by_css_selector("a[class='logout']")

    def navigate_to_login_page(self):
        self.log.info("Clicked on Login page {}".format(self.click(Login.login_button)))
        self.time_sleep(sleep_time)

    def login(self,email,password):
        self.driver_wait(wait_time)
        self.enter_text(Login.email_field, text=email)
        self.log.info("Entered the email {}".format(email))
        self.enter_text(Login.password_field, text=password)
        self.log.info("Entered the password {}".format(password))
        self.log.info("Clicked the submit button {}".format(self.click(Login.submit_button)))

    def logout(self):
        self.log.info("Clicked the logout button {}".format(self.click(Login.logout_button)))




    #def navigate_to_login_page(self):
     #   self.driver.find_element(*Login.login_btton).click()  #Here * is to deserialize the tuple.


