from selenium.webdriver.common.by import By
import pytest

from config import wait_time
from page_objects.common import Common
from page_objects.item_search import Search_Item
from page_objects.login import Login
from utilities import driver
import allure

@allure.feature('Search Item')
class TestSearchItem:

    @allure.story('Search the item')
    def test_searchbar(self,driver):
        l = Login(driver)
        c = Common(driver)
        s = Search_Item(driver)
        c.driver_wait(wait_time)
        s.item_search()




