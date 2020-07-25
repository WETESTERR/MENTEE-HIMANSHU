import json
import os

from page_objects.common import Common
from utilities import driver
from utilities.locator_strategy import LocatorStrategy
import config

class Search_Item(Common):



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver



    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")

    def item_search(self):
        with open(config.project_root + '\\json_utilities\\data.json') as f:
            data_file = json.loads(f.read())
        self.enter_text(Search_Item.search_field, text=data_file['item'])
        self.click(Search_Item.search_button)