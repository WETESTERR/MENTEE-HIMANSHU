import config
from page_objects.common import Common
from utilities.locator_strategy import LocatorStrategy


class CreateUser(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_button = LocatorStrategy.locator_by_xpath("//a[@class='login']")
    email_field = LocatorStrategy.locator_by_id("email_create")
    submit_button = LocatorStrategy.locator_by_id("SubmitCreate")
    gender = LocatorStrategy.locator_by_xpath("//input[@id='id_gender1']")
    first_name = LocatorStrategy.locator_by_xpath("//*[@id='customer_firstname']")
    last_name = LocatorStrategy.locator_by_css_selector("input[name='customer_lastname']")
    password_field = LocatorStrategy.locator_by_name("passwd")
    date_dob = LocatorStrategy.locator_by_id("days")
    month_dob = LocatorStrategy.locator_by_css_selector("#months")
    year_dob = LocatorStrategy.locator_by_css_selector("#years")
    address_firstname = LocatorStrategy.locator_by_id("firstname")
    address_lastname = LocatorStrategy.locator_by_id("lastname")
    address_number = LocatorStrategy.locator_by_css_selector("#address1")
    address_city = LocatorStrategy.locator_by_css_selector("input[name='city']")
    address_state = LocatorStrategy.locator_by_id("id_state")
    address_postcode = LocatorStrategy.locator_by_id("postcode")
    address_country = LocatorStrategy.locator_by_id("id_country")
    phone_num = LocatorStrategy.locator_by_xpath("//*[@id = 'phone_mobile']")
    alias = LocatorStrategy.locator_by_id("alias")
    submit = LocatorStrategy.locator_by_id("submitAccount")


    def login_click(self):
        self.click(CreateUser.login_button)


    def enter_email(self,email):
        self.enter_text(CreateUser.email_field,text=email)
        self.click(CreateUser.submit_button)


    def title(self,password):
        self.driver_wait(config.wait_time)
        self.click(CreateUser.gender)
        self.enter_text(CreateUser.first_name, text="Himanshu")
        self.enter_text(CreateUser.last_name, text="Sethi")
        self.enter_text(CreateUser.password_field, text=password)


    def date_of_birth(self):
        date = self.select_option_from_drop_down(CreateUser.date_dob)
        date.select_by_index(7)
        month = self.select_option_from_drop_down(CreateUser.month_dob)
        month.month.select_by_index(9)
        year = self.select_option_from_drop_down(CreateUser.year_dob)
        year.year.select_by_value('1988')


    def address(self):
        self.clear(CreateUser.address_firstname)
        self.enter_text(CreateUser.address_firstname, text="Him")
        self.clear(CreateUser.address_lastname)
        self.enter_text(CreateUser.address_lastname, text = "Seth")
        self.enter_text(CreateUser.address_number, text = "123")
        self.enter_text(CreateUser.address_city, text = "Fairfax")
        state = self.select_option_from_drop_down(CreateUser.address_state)
        state.select_by_visible_text("Virginia")
        self.enter_text(CreateUser.address_postcode, text="22030")
        country = self.select_option_from_drop_down(CreateUser.address_country)
        country.select_by_visible_text("United States")


    def misc_info(self):
        self.enter_text(CreateUser.phone_num, text = "1234567890")
        self.enter_text(CreateUser.alias, text="My address")
        self.click(CreateUser.submit)






