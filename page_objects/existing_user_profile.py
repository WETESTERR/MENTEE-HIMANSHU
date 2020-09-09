from page_objects.common import Common
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy


class ExistingUser(Common):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.data = DataRead.json_read('data.json')


    login_button = LocatorStrategy.locator_by_class_name('login')
    email_field = LocatorStrategy.locator_by_id("email_create")
    submit_button = LocatorStrategy.locator_by_id("SubmitCreate")

    def login_click(self):
        self.click(ExistingUser.login_button)


    def enter_email(self):
        self.enter_text(ExistingUser.email_field,text=self.data['existing_email'])
        self.click(ExistingUser.submit_button)
        self.log.info("Entered email is {}".format(self.data['existing_email']))
        self.get_screenshot(file_name="Existing_User")