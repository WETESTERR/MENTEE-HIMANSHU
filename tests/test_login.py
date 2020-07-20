import allure
import pytest

from page_objects.login import Login
from utilities.log import Logs



@allure.feature('Login Feature')
class TestLogin(Logs):

    @allure.story('Login functions')
    def test_login(self,driver,email,password):
        log = self.logger()

        l = Login(driver)
        log.info(l)
        l.navigate_to_login_page()
        l.login_verify(email,password)







