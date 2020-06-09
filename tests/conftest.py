import pytest

from selenium import webdriver


class baseSetup:

    global driver

    def pytest_addoption(parser):
        parser.addoption(
            "--browser_name", action="store", default="chrome"
        )

    @pytest.fixture(scope="module")
    def driverSetup(self,request):
        self.request = request

        browser_name = request.config.getoption("browser_name")
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\Users\\Himanshu\\Downloads\\chromedriver.exe")
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path="path")
        elif browser_name == "IE":
            driver = webdriver.Ie(executable_path="path")

        request.cls.driver = driver
        yield
        driver.close()








