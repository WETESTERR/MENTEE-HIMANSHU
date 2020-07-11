import time
import traceback

import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from utilities import driver, log
import config
from utilities.log import Logs



class Common(Logs):

    def __init__(self,driver):
        self.driver = driver
        self.log = self.logger()



    def driver_wait(self,wait_time):
        self.log.info(WebDriverWait(self.driver, wait_time))

    def time_sleep(self,sleep_time):
        self.log.info(time.sleep(sleep_time))

    def click(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            _element.click()

        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))

        self.log.info(_element)

    def enter_text(self,locatorobject,text):
        _element = self.get_element(locatorobject)
        if _element:
            _element.send_keys(text)
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_stack()))
        self.log.info(_element)

    def verify_link_presence(self,wait_time,text,*locator):
        self.log.info(WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located((*locator,text))))


    def switch_frame(self,value):
        self.log.info(self.driver.switch_to.frame(value))


    def drop_down(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            Select(_element)
        else:
            pytest.fail('Element not found \n{}'.format(traceback.extract_stack()))
        self.log.info(_element)


    def switch_window(self,text):
        self.log.info(self.driver.switch_to_window(text))
        self.driver.switch_to_default_content()

    def verify_text_present(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText in gettext
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))
        self.log.info(_element)

    def verify_exact_text(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText == gettext
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))
        self.log.info(_element)

    def drag_drop(self,source,target):
        source_element = self.driver.find_element_by_name(source)
        self.log.info(source_element)
        target_element = self.driver.find_element_by_name(target)
        self.log.info(target_element)

        action_chains = ActionChains(driver)
        self.log.info(action_chains.drag_and_drop(source_element,target_element).perform())

    def log_test_start(self):
        pass

    def log_test_end(self):
        pass

    def get_element(self,locatorobject):
        if locatorobject.strategy == 'id':
            return self.driver.find_element_by_id(locatorobject.name)
        elif locatorobject.strategy == 'xpath':
            return self.driver.find_element_by_xpath(locatorobject.name)
        elif locatorobject.strategy == 'css_selector':
            return self.driver.find_element_by_css_selector(locatorobject.name)
        elif locatorobject.strategy == 'class_name':
            return self.driver.find_element_by_class_name(locatorobject.name)
        elif locatorobject.strategy == 'name':
            return self.driver.find_element_by_name(locatorobject.name)
        elif locatorobject.strategy == 'link_text':
            return self.driver.find_element_by_link_text(locatorobject.name)
        elif locatorobject.strategy == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(locatorobject.name)
        elif locatorobject.strategy == 'index':
            return self.driver.find_element_by_index(locatorobject.name)
        elif locatorobject.strategy == 'value':
            return self.driver.find_element_by_value(locatorobject.name)
        elif locatorobject.strategy == 'visible_text':
            return self.driver.find_element_by_visible_text(locatorobject.name)


