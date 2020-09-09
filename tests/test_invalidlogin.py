import allure
import pytest

from page_objects.login import Login

@allure.feature("Invalid Login")
class TestInvalidlogin:

    @allure.story("Login with invalid credentials fails")
    @pytest.mark.skip("Skip for now")
    def test_invalid_login(self,driver):
        l = Login(driver)
        l.logout()
        l.invalid_login_verify()