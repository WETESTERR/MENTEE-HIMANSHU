from selenium.webdriver.common.by import By
import pytest

from config import wait_time
from page_objects.common import Common
from page_objects.login import Login
from utilities import driver



class TestSearchItem:

    @pytest.mark.skip("Just a Test Browser.")
    def test_searchbar(self,driver):
        l = Login(driver)
        c = Common(driver)
        c.driver_wait(wait_time)
        c.enter_text(By.ID,"search_query_top",text='Printed Dress')
        c.click(By.XPATH, "//button[@name='submit_search']")
        l.items()
        l.select_items()



