import allure
import pytest

from page_objects.create_user import CreateUser
from page_objects.login import Login


@allure.feature("Create User")
class TestCreateUser:

    @allure.story("Enter user details")
    #@pytest.mark.skip("Skip for now")
    @pytest.mark.last
    def test_createuser(self,driver,password):
        c = CreateUser(driver)
        l = Login(driver)
        l.logout()
        c.login_click()
        c.enter_email()
        c.fill_title_info(password)
        c.fill_date_of_birth()
        c.fill_address_details()
        c.misc_info()