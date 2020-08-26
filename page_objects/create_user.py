import config
from page_objects.common import Common
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy


class CreateUser(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = DataRead.json_read('data.json')

    login_button = LocatorStrategy.locator_by_class_name('login')
    email_field = LocatorStrategy.locator_by_id("email_create")
    submit_button = LocatorStrategy.locator_by_id("SubmitCreate")
    gender = LocatorStrategy.locator_by_id("id_gender1")
    first_name = LocatorStrategy.locator_by_id("customer_firstname")
    last_name = LocatorStrategy.locator_by_name("customer_lastname")
    password_field = LocatorStrategy.locator_by_name("passwd")
    date_dob = LocatorStrategy.locator_by_id("days")
    month_dob = LocatorStrategy.locator_by_css_selector("#months")
    year_dob = LocatorStrategy.locator_by_css_selector("#years")
    address_firstname = LocatorStrategy.locator_by_id("firstname")
    address_lastname = LocatorStrategy.locator_by_id("lastname")
    address_number = LocatorStrategy.locator_by_css_selector("#address1")
    address_city = LocatorStrategy.locator_by_name("city")
    address_state = LocatorStrategy.locator_by_id("id_state")
    address_postcode = LocatorStrategy.locator_by_id("postcode")
    address_country = LocatorStrategy.locator_by_id("id_country")
    phone_num = LocatorStrategy.locator_by_name("phone_mobile")
    alias = LocatorStrategy.locator_by_id("alias")
    submit = LocatorStrategy.locator_by_id("submitAccount")


    def login_click(self):
        self.click(CreateUser.login_button)


    def enter_email(self,email):
        self.enter_text(CreateUser.email_field,text=self.data['new_email'])
        self.click(CreateUser.submit_button)


    def title_info(self,password):
        self.time_sleep(config.sleep_time)
        self.click(CreateUser.gender)
        self.enter_text(CreateUser.first_name, text=self.data['firstname'])
        self.enter_text(CreateUser.last_name, text=self.data['lastname'])
        self.enter_text(CreateUser.password_field, text=password)


    def date_of_birth(self):
        select = self.select_option_from_drop_down(CreateUser.date_dob)
        select.select_by_index(7)
        select = self.select_option_from_drop_down(CreateUser.month_dob)
        select.select_by_index(9)
        select = self.select_option_from_drop_down(CreateUser.year_dob)
        select.select_by_value('1988')


    def address(self):
        self.clear_text(CreateUser.address_firstname)
        self.enter_text(CreateUser.address_firstname, text=self.data['firstname'])
        self.clear_text(CreateUser.address_lastname)
        self.enter_text(CreateUser.address_lastname, text = self.data['lastname'])
        self.enter_text(CreateUser.address_number, text = self.data['house_number'])
        self.enter_text(CreateUser.address_city, text = self.data['city'])
        select = self.select_option_from_drop_down(CreateUser.address_state)
        select.select_by_visible_text("Virginia")
        self.enter_text(CreateUser.address_postcode, text=self.data['postcode'])
        select = self.select_option_from_drop_down(CreateUser.address_country)
        select.select_by_visible_text("United States")


    def misc_info(self):
        self.enter_text(CreateUser.phone_num, text = self.data['phone_number'])
        self.enter_text(CreateUser.alias, text=self.data['alias_text'])
        self.click(CreateUser.submit)






