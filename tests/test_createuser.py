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
        c.title_info(password)
        c.date_of_birth()
        c.address()
        c.misc_info()
