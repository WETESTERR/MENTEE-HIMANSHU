import pytest

from page_objects.item_details import ItemDetails


class TestQuantity:

    #@pytest.mark.skip("Skip for now")
    def test_add_quantity(self,driver):
        i = ItemDetails(driver)
        i.item_search()
        i.product_details()
        i.add_quantity()


    def test_negative_quantity(self,driver):
        i=ItemDetails(driver)
        i.delete_quantity()
