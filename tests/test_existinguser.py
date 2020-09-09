import allure

from page_objects.existing_user_profile import ExistingUser
from page_objects.login import Login

@allure.feature("Existing User")
class TestExistingUser:

    @allure.story("Entering existing user to create new user fails")
    def test_existing_user(self,driver):
        e = ExistingUser(driver)
        l = Login(driver)
        l.logout()
        e.login_click()
        e.enter_email()

