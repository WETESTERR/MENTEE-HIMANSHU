import allure

from config import wait_time
from page_objects.common import Common
from page_objects.home_page import HomePage
from page_objects.item_search import Search_Item

@allure.feature('Item Ship')
class TestShipping:

    @allure.story("Clicking the Terms of Service and Proceed to checkout")
    def test_shipping_page(self,driver):
        c = Common(driver)
        s = Search_Item(driver)
        h = HomePage(driver)
        h.navigate_to_homepage()
        c.driver_wait(wait_time)
        s.item_search()
        s.add_item()
        s.proceed_to_checkout()
        s.shopping_cart_checkout()
        s.shipping_page_checkout()
