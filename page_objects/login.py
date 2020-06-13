
from selenium.webdriver.common.by import By






class Login:


    def __init__(self,driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.find_element(By.XPATH,"//a[@class='login']").click()

    def login(self,email,password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        #self.driver.send_keys(emailfield,email)
        self.driver.find_element(By.ID, "passwd").send_keys(password)
       # self.driver.send_keys(passwordfield,password)
        self.driver.find_element(By.NAME, "SubmitLogin").click()

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[class='logout']").click()




