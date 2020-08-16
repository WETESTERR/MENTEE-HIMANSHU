import pytest

import config
from page_objects.common import Common
from page_objects.login import Login

from utilities.driver import Driver


d = Driver()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--email", action="store", required=True)
    parser.addoption("--password", action="store", required=True)


@pytest.fixture(scope='session', autouse=True)
def browser_name(request):
    return request.config.getoption("--browser_name")


@pytest.fixture(scope='session')
def driver(browser_name):
    _driver = d.get_driver(browser_name)
    d.launch_url(config.url, _driver)
    return _driver


# def teardown():
#    d.quit_driver(_driver)
# request.add_finalizer(teardown)

@pytest.fixture(scope='session', autouse=True)
def email(request):
    return request.config.getoption("--email")


@pytest.fixture(scope='session', autouse=True)
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope='session',autouse=True)
def setup(driver,email,password):
    l = Login(driver)
    l.navigate_to_login_page()
    l.login_verify(email,password)


