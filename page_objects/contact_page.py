import config
from page_objects.common import Common
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy

class Contact(Common):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = DataRead.json_read('data.json')


    contact_button = LocatorStrategy.locator_by_id("contact-link")
    text_message = LocatorStrategy.locator_by_id("message")
    subject_heading = LocatorStrategy.locator_by_id("id_contact")
    email_address = LocatorStrategy.locator_by_id("email")
    send_button = LocatorStrategy.locator_by_id("email")
    upload_file = LocatorStrategy.locator_by_id("fileUpload")


    def contact_us_form(self):
        self.click(Contact.contact_button)
        self.enter_text(Contact.text_message, text="This is a test.")
        select = self.select_option_from_drop_down(Contact.subject_heading)
        select.select_by_index(1)
        self.clear_text(Contact.email_address)
        self.enter_text(Contact.email_address,text=self.data['contact_email'])
        self.enter_text(Contact.upload_file,text=self.data['upload_file'])
        self.click(Contact.send_button)


