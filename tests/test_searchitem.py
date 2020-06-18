from selenium.webdriver.common.by import By
import pytest

from config import wait_time
from page_objects.common import Common
from page_objects.login import Login
from utilities import driver



class TestSearchItem:

    def test_searchbar(self,driver):

        c = Common(driver)
        c.driver_wait(wait_time)
        #c.click(By.ID,"search_query_top")
        c.enter_text(By.ID,"search_query_top",text='iPhone')

