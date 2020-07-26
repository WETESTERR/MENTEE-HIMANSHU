import json
import os

from page_objects.common import Common
from utilities import driver
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy
import config


class Search_Item(Common,DataRead):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")

    def item_search(self):
        data = self.json_read('\\json_utilities\\data.json')
        self.enter_text(Search_Item.search_field, text=data['item'])
        self.click(Search_Item.search_button)
