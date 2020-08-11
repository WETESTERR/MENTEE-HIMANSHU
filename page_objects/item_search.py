import json
import os

from page_objects.common import Common
from utilities import driver
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy
from config import sleep_time, wait_time, test_data_path


class Search_Item(Common):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #d = DataRead()
        self.data = DataRead.json_read('data.json')

    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")
    product = LocatorStrategy.locator_by_xpath("//div[@class='product-container']/div[1]/div/a/img")
    add_to_cart = LocatorStrategy.locator_by_xpath("//div[@class='product-container']/div[2]/div[2]/a[@title='Add to cart']")
    checkout_button = LocatorStrategy.locator_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a")
    shopping_cart_checkout_button = LocatorStrategy.locator_by_xpath("//*[@id='center_column']/p[2]/a[1]/span")
    address_page_checkout_button = LocatorStrategy.locator_by_xpath("//*[@class='columns-container']/div/div[3]/div/form/p/button/span")

    def item_search(self):
        self.enter_text(Search_Item.search_field, text=self.data['item'])
        self.click(Search_Item.search_button)

    def add_item(self):
        self.actions(move1=Search_Item.product,move2=Search_Item.add_to_cart)


    def proceed_to_checkout(self):
        self.time_sleep(sleep_time)
        self.click(Search_Item.checkout_button)


    def shopping_cart_checkout(self):
        self.time_sleep(sleep_time)
        self.click(Search_Item.shopping_cart_checkout_button)


    def address_page_checkout(self):
        self.click(Search_Item.address_page_checkout_button)



