import pytest

from selenium import webdriver


@pytest.mark.usefixtures("driversetup")

def browser(self,driver):
    return self.driver.get("http://automationpractice.com/index.php")
    return self.driver.maximize_window()





