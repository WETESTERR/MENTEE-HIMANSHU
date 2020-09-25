import allure
import pytest

from page_objects.home_page import HomePage
from page_objects.login import Login

@allure.feature("Invalid Login")
class TestInvalidlogin:

    @allure.story("Login with invalid credentials fails")
    #@pytest.mark.skip("Skip for now")
    @pytest.mark.last
    def test_invalid_login(self,driver):
        l = Login(driver)
        #l.logout()
        #l.navigate_to_login_page()
        l.invalid_login_verify()