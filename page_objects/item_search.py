from page_objects.common import Common
from utilities import driver
from utilities.locator_strategy import LocatorStrategy

class Search_Item(Common):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")

    def item_search(self):
        self.enter_text(Search_Item.search_field, text="Printed Dress")
        self.click(Search_Item.search_button)