import pytest

from page_objects.home_page import HomePage
from page_objects.item_details import ItemDetails
from page_objects.login import Login


class TestProductDetails:

    @pytest.mark.skip("Skip for now")
    def test_product_details(self, driver):
        s = ItemDetails(driver)
        h = HomePage(driver)
        h.navigate_to_homepage()
        s.item_search()
        s.product_details()
        s.product_review_form()
        s.add_item_to_cart()
