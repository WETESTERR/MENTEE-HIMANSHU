import self
from selenium.webdriver.common.by import By

from page_objects.common import Common
from utilities import driver


class Login(Common):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    login_btton = (By.XPATH,"//a[@class='login']")
    email_field = (By.ID, "email")
    password_field = (By.ID, "passwd")
    submit_button = (By.NAME, "SubmitLogin")
    logout_button = (By.CSS_SELECTOR,"a[class='logout']")

    #def navigate_to_login_page(self):
     #   self.driver.find_element(*Login.login_btton).click()      #Here * is to deserialize the tuple.
    def navigate_to_login_page(self):
        self.click(*Login.login_btton)
        self.time_sleep()

    def login(self,email,password):
        self.driver_wait()
        self.enter_text(*Login.email_field,text = email)
        self.enter_text(*Login.password_field,text = password)
        #self.driver.find_element(*Login.email_field).send_keys(email)
        #self.driver.find_element(*Login.password_field).send_keys(password)
        self.click(*Login.submit_button)

    def logout(self):
        self.click(*Login.logout_button)




