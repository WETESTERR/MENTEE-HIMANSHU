import pytest

from selenium import webdriver

from tests.conftest import baseSetup


@pytest.mark.usefixtures("driverSetup")
class browser():
    def browser(self):
        self.driver.get("http://automationpractice.com/index.php")
        return self.driver.maximize_window()