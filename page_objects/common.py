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
        WebDriverWait(self.driver, wait_time)
        self.log.info("Webdriver wait {}".format(wait_time))

    def time_sleep(self,sleep_time):
        time.sleep(sleep_time)
        self.log.info("Sleep time {}".format(sleep_time))

    def click(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            _element.click()
            self.log.info("Clicked on the element {}".format(locatorobject.name))
        else:
            self.log.error('Element not found \n{}'.format(traceback.format_exc()))
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))


    def enter_text(self,locatorobject,text):
        _element = self.get_element(locatorobject)
        if _element:
            _element.send_keys(text)
            self.log.info("Entered text element {}".format(locatorobject.name))
        else:
            self.log.error('Element not found \n{}'.format(traceback.format_stack()))
            pytest.fail('Element not found \n{}'.format(traceback.format_stack()))


    def verify_link_presence(self,wait_time,text,*locator):
        self.log.info("Verifying the presence of link {}".format(WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located((*locator,text)))))


    def switch_frame(self,value):
        self.driver.switch_to.frame(value)
        self.log.info("Switch frame value {}".format(self.driver.switch_to.frame(value)))


    def select_option_from_drop_down(self,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            Select(_element)
            self.log.info("Drop down element {}".format(locatorobject.name))
        else:
            self.log.error('Element not found \n{}'.format(traceback.extract_stack()))
            pytest.fail('Element not found \n{}'.format(traceback.extract_stack()))



    def switch_window(self,text):
        self.log.info("Window switch {}".format(self.driver.switch_to_window(text)))
        self.driver.switch_to_default_content()

    def verify_text_present(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText in gettext
            self.log.info("Verifying the presence of text {}".format(locatorobject.name))
        else:
            self.log.error('Element not found \n{}'.format(traceback.format_stack()))
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))


    def verify_exact_text(self,validateText,locatorobject):
        _element = self.get_element(locatorobject)
        if _element:
            gettext = _element.text
            assert validateText == gettext
            self.log.info("Verifying the exact text {}".format(locatorobject.name))
        else:
            self.log.error('Element not found \n{}'.format(traceback.format_exc()))
            pytest.fail('Element not found \n{}'.format(traceback.format_exc()))


    def drag_drop(self,source,target):
        source_element = self.driver.find_element_by_name(source)
        self.log.info("Grabbed the source element {}".format(source_element))
        target_element = self.driver.find_element_by_name(target)
        self.log.info("Grabbed the target element {}".format(target_element))

        action_chains = ActionChains(driver)
        self.log.info("Drag and Drop {}".format(action_chains.drag_and_drop(source_element,target_element).perform()))

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

    def get_screenshot(self,file_name):
        self.driver.get_screenshot_as_file(file_name)

