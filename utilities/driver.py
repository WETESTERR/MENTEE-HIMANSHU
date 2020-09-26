import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
#from webdrivermanager import EdgeDriverManager

import config


class Driver:

    def get_driver(self,browser_name):

        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "IE":
            driver = webdriver.Ie(executable_path=IEDriverManager().install())
        elif browser_name == "edge":
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        else:
            raise RuntimeError("Browser not found : {}".format(browser_name))  #If there is a spelling error while entering the browser_name, this exception will invoke.
        return driver

#These are functions to call the url from config.py file and driver.
    def launch_url(self,url,driver):
        driver.get(url)
        driver.maximize_window()


    def quit_driver(self,driver):
        driver.quit()




