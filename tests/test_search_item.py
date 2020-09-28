import allure
from selenium.webdriver.common.by import By
import pytest

from config import wait_time
from page_objects.common import Common
from page_objects.home_page import HomePage
from page_objects.item_search import SearchItem
from page_objects.login import Login
from utilities import driver


@allure.feature('Item Seach')
class TestSearchItem:

    @allure.story('Search Item and Add Item')
    @pytest.mark.smoke
    @pytest.mark.searchbar
    @pytest.mark.skip("Skip for now")
    #@pytest.mark.first
    def test_searchbar(self,driver):
        c = Common(driver)
        s = SearchItem(driver)
        h = HomePage(driver)
        l = Login(driver)
        h.navigate_to_homepage()
        c.driver_wait(wait_time)
        s.item_search()
        s.add_item()
        s.proceed_to_checkout()
        s.shopping_cart_checkout()







