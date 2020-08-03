import pytest


import config

from utilities.driver import Driver

d = Driver()



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--email",action = "store",required=True)
    parser.addoption("--password", action="store",required=True)

@pytest.fixture(scope='session', autouse=True)
def browser_name(request):
    return request.config.getoption("--browser_name")

@pytest.fixture(scope='session')
def driver(request,browser_name):
    _driver = d.get_driver(browser_name)      # _driver is a provate variable for this function only.
    d.launch_url(config.url,_driver)          #Here we created the global variable d for the class Driver from driver.py file and call the get_driver and launch_url function.
    return _driver
   #def teardown():
    #    d.quit_driver(_driver)
    #request.add_finalizer(teardown)

@pytest.fixture(scope='session', autouse=True)
def email(request):
    return request.config.getoption("--email")


@pytest.fixture(scope='session', autouse=True)
def password(request):
    return request.config.getoption("--password")

@pytest.mark.usefixtures("driversetup")
def browser(self,driver):
    return self.driver.get("http://automationpractice.com/index.php")
    return self.driver.maximize_window()






