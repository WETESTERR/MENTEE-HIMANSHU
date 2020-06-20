import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from utilities import driver
import config


class Common:

    def __init__(self,driver):
        self.driver = driver

    def driver_wait(self,wait_time):
        WebDriverWait(self.driver,wait_time)

    def time_sleep(self,sleep_time):
        time.sleep(sleep_time)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def enter_text(self,*locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def verify_link_presence(self,wait_time,text,*locator):
        WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located((*locator,text)))

    def switch_frame(self,value):
        self.driver.switch_to.frame(value)

    def drop_down_selectby_name(self,text):
        Select(self.driver.find_element_by_name(text))

    def drop_down_selectby_index(self,text):
        Select(self.driver.find_element_by_index(text))

    def drop_down_selectby_value(self,text):
        Select(self.driver.find_element_by_value(text))

    def drop_down_selectby_visible_text(self,text):
        Select(self.driver.find_element_by_visible_text(text))


    def switch_window(self,text):
        self.driver.switch_to_window(text)
        self.driver.switch_to_default_content()

    def verify_text(self,validateText,*locator):
        gettext = self.driver.find_element(*locator).text
        assert validateText in gettext

    def verify_exact_text(self,validateText,*locator):
        gettext = self.driver.find_element(*locator).text
        assert validateText == gettext

    def drag_drop(self,source,target):
        source_element = self.driver.find_element_by_name(source)
        target_element = self.driver.find_element_by_name(target)

        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(source_element,target_element).perform()


        