import time
import traceback

import pytest
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

    def click(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            _element.click()
            #TODO include log statement
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))
            #TODO try other traceback methods

    def enter_text(self,locatorobject,text):
        _element = self.get_element(locatorobject)
        if _element:
            _element.send_keys(text)
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_stack()))

    def verify_link_presence(self,wait_time,text,*locator):
        WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located((*locator,text)))

    def switch_frame(self,value):
        self.driver.switch_to.frame(value)

    # TODO create one drop_down method with the locator_strategy

    def drop_down(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            Select(_element)
        else:
            pytest.fail('Element not found \n{}'.format(traceback.extract_stack()))


    def switch_window(self,text):
        self.driver.switch_to_window(text)
        self.driver.switch_to_default_content()

    def verify_text(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText in gettext
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))

    def verify_exact_text(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText == gettext
        else:
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))

    def drag_drop(self,source,target):
        source_element = self.driver.find_element_by_name(source)
        target_element = self.driver.find_element_by_name(target)

        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(source_element,target_element).perform()

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

        #TODO Implement for all other locators from locator_strategy
