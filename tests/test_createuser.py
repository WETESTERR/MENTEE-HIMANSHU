import allure
import pytest

from page_objects.create_user import CreateUser
from page_objects.login import Login


@allure.feature("Create User")
class TestCreateUser:

    @allure.story("Enter user details")
    #@pytest.mark.skip("Skip for now")
    def test_createuser(self,driver,email,password):
        c = CreateUser(driver)
        l = Login(driver)
        l.logout()
        c.login_click()
        c.enter_email(email)
        c.fill_title_info(password)
        c.fill_date_of_birth()
        c.fill_address_details()
        c.misc_info()
