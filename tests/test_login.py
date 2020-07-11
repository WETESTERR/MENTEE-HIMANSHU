import pytest

from page_objects.login import Login
from utilities.log import Logs




class TestLogin(Logs):

    def test_login(self,driver,email,password):
        log = self.logs()

        l = Login(driver)
        log.info(l)
        l.navigate_to_login_page()
        l.login(email,password)







