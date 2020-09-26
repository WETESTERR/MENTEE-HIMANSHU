import allure
import pytest

from page_objects.existing_user_profile import ExistingUser
from page_objects.login import Login

@allure.feature("Existing User")
class TestExistingUser:

    @allure.story("Entering existing user to create new user fails")
    #@pytest.mark.skip("Skip for now")
    @pytest.mark.second_to_last
    def test_existing_user(self,driver):
        e = ExistingUser(driver)
        l = Login(driver)
        l.logout()
        e.login_click()
        e.enter_email()

