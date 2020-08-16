from page_objects.common import Common
from utilities.locator_strategy import LocatorStrategy

class HomePage(Common):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    logo = LocatorStrategy.locator_by_xpath("//*[@class='logo img-responsive']")

    def navigate_to_homepage(self):
        self.click(HomePage.logo)
