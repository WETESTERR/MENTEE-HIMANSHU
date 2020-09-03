import config
from page_objects.common import Common
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy
from config import sleep_time, wait_time, test_data_path


class SearchItem(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # d = DataRead()
        self.data = DataRead.json_read('data.json')

    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")
    product = LocatorStrategy.locator_by_xpath("//div[@class='product-container']/div[1]/div/a/img")
    add_to_cart = LocatorStrategy.locator_by_xpath(
        "//div[@class='product-container']/div[2]/div[2]/a[@title='Add to cart']")
    checkout_button = LocatorStrategy.locator_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a")
    product_description = LocatorStrategy.locator_by_class_name("product-name")
    shopping_cart_checkout_button = LocatorStrategy.locator_by_xpath("//*[@id='center_column']/p[2]/a[1]/span")
    address_page_checkout_button = LocatorStrategy.locator_by_xpath(
        "//*[@class='columns-container']/div/div[3]/div/form/p/button/span")
    shipping_page_terms = LocatorStrategy.locator_by_id("cgv")
    shipping_page_checkout_button = LocatorStrategy.locator_by_xpath(
        "//*[@class='columns-container']/div/div[3]/div/div/form/p/button/span")
    payment_page_button = LocatorStrategy.locator_by_xpath("//*[@class='bankwire']")
    confirm_button = LocatorStrategy.locator_by_css_selector("#cart_navigation > button")
    complete_status = LocatorStrategy.locator_by_xpath("//*[@class='box']/p")

    def item_search(self):
        self.enter_text(SearchItem.search_field, text=self.data['item'])
        self.click(SearchItem.search_button)

    def add_item(self):
        self.driver_wait(config.wait_time)
        self.actions(move1=SearchItem.product, move2=SearchItem.add_to_cart)

    def proceed_to_checkout(self):
        self.time_sleep(config.sleep_time)
        self.click(SearchItem.checkout_button)

    def shopping_cart_checkout(self):
        self.driver_wait(config.wait_time)
        if self.verify_exact_text(SearchItem.product_description,self.data['dress_name']):
            self.click(SearchItem.shopping_cart_checkout_button)

    def address_page_checkout(self):
        self.time_sleep(config.sleep_time)
        self.click(SearchItem.address_page_checkout_button)

    def shipping_page_checkout(self):
        self.driver_wait(config.wait_time)
        self.click(SearchItem.shipping_page_terms)
        self.click(SearchItem.shipping_page_checkout_button)

    def confirm_order(self):
        self.click(SearchItem.payment_page_button)
        self.click(SearchItem.confirm_button)

    def order_status(self):
        self.verify_text_present(SearchItem.complete_status, validatetext='complete')
