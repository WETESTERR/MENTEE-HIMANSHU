import time

import pytest
import self
from selenium.webdriver.common.by import By

from config import sleep_time, wait_time
from page_objects.common import Common
from utilities import driver


class Login(Common):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_btton = (By.XPATH,"//a[@class='login']")
    email_field = (By.ID, "email")
    password_field = (By.ID, "passwd")
    submit_button = (By.NAME, "SubmitLogin")
    logout_button = (By.CSS_SELECTOR,"a[class='logout']")

    #def navigate_to_login_page(self):
     #   self.driver.find_element(*Login.login_btton).click()      #Here * is to deserialize the tuple.

    def navigate_to_login_page(self):
        self.click(*Login.login_btton)
        self.time_sleep(sleep_time)


    def login(self,email,password):
        self.driver_wait(wait_time)
        self.enter_text(*Login.email_field,text = email)
        self.enter_text(*Login.password_field,text = password)
        self.click(*Login.submit_button)


    def logout(self):
        self.click(*Login.logout_button)

    def items(self):
        count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-container']"))
        assert count == 5

    def select_items(self):
        items = self.driver.find_elements(By.XPATH, "//div[@class='product-container']")
        button = self.driver.find_elements(By.XPATH,"//a[@title='Add to cart']")
        for item in items:
            itemtext = self.driver.find_elements(By.XPATH,"//a[@title='Printed Summer Dress']")
            if itemtext == 'Printed Summer Dress':
                button.click()





