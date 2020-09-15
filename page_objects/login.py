import time


import pytest
from selenium.webdriver.common.by import By

from config import sleep_time, wait_time
from page_objects.common import Common
from utilities import driver
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy




class Login(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = DataRead.json_read('data.json')

    login_button = LocatorStrategy.locator_by_xpath("//a[@class='login']")
    email_field = LocatorStrategy.locator_by_id("email")
    password_field = LocatorStrategy.locator_by_id("passwd")
    submit_button = LocatorStrategy.locator_by_name("SubmitLogin")
    logout_button = LocatorStrategy.locator_by_css_selector("a[class='logout']")


    def navigate_to_login_page(self):
        self.click(Login.login_button)
        self.get_screenshot(file_name="Login_page")
        self.time_sleep(sleep_time)

    def login_verify(self,email,password):
        self.driver_wait(wait_time)
        self.enter_text(Login.email_field, text=email)
        self.enter_text(Login.password_field, text=password)
        self.click(Login.submit_button)
        self.verify_element_present(Login.logout_button)

    def invalid_login_verify(self):
        self.driver_wait(wait_time)
        self.enter_text(Login.email_field, text=self.data["invalid_email"])
        self.enter_text(Login.password_field, text=self.data["invalid_password"])
        self.click(Login.submit_button)
        self.get_screenshot("Invalid Username or Password")

    def logout(self):
        self.click(Login.logout_button)




    #def navigate_to_login_page(self):
     #   self.driver.find_element(*Login.login_btton).click()  #Here * is to deserialize the tuple.


