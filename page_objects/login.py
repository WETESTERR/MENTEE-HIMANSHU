from selenium.webdriver.common.by import By

from selenium import webdriver



from utilities import driver


class Login:

    loginemail = (By.CSS_SELECTOR, "input[id='email']")
    loginpwd = (By.ID, "passwd")


    def __init__(self,driver):
        self.driver = driver

    def loginbutton(self):
        self.driver.find_element(By.XPATH,"//a[@class='login']")


    def submitbutton(self):
        self.driver.find_element(By.NAME,"SubmitLogin")


    def logoutbutton(self):
        self.driver.find_element(By.XPATH,"//a[@class='logout']")

