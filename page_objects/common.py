import time

from selenium.webdriver.support.wait import WebDriverWait

from utilities import driver


class Common:

    def __init__(self,driver):
        self.driver = driver

    def driver_wait(self):
        WebDriverWait(self.driver,10)

    def time_sleep(self):
        time.sleep(5)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def enter_text(self,*locator,text):
        self.driver.find_element(*locator).send_keys(text)
