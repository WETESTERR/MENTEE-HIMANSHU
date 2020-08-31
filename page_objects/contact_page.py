from page_objects.common import Common
from utilities.locator_strategy import LocatorStrategy

class Contact(Common):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    contact_button = LocatorStrategy.locator_by_id("contact-link")


    def contact_us_form(self):
        self.click(Contact.contact_button)
