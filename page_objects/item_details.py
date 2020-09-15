import config
from page_objects.common import Common
from utilities.data_factory import DataRead
from utilities.locator_strategy import LocatorStrategy


class ItemDetails(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = DataRead.json_read('data.json')

    search_field = LocatorStrategy.locator_by_id("search_query_top")
    search_button = LocatorStrategy.locator_by_xpath("//button[@name='submit_search']")
    more_options = LocatorStrategy.locator_by_xpath("//div[@class='product-container']/div[2]/div[2]/a[@title='View']")
    select_size = LocatorStrategy.locator_by_id("group_1")
    products = LocatorStrategy.locator_by_xpath("//div[@class='product-container']/div[1]/div/a/img")
    prod_name = LocatorStrategy.locator_by_xpath("//*[@id='center_column']/ul/li[3]/div/div[2]/h5/a")
    datasheet_properties = LocatorStrategy.locator_by_xpath("//*[@class='page-product-box']/table/tbody/tr[3]/td[2]")
    dress_name = LocatorStrategy.locator_by_xpath("//*[@id='center_column']/div/div/div[3]/h1")
    change_color = LocatorStrategy.locator_by_id("color_13")
    write_review = LocatorStrategy.locator_by_class_name("open-comment-form")
    review_title = LocatorStrategy.locator_by_id("comment_title")
    comment = LocatorStrategy.locator_by_id("content")
    send_button = LocatorStrategy.locator_by_id("submitNewMessage")
    comment_ok = LocatorStrategy.locator_by_xpath("//*[@id='product']/div[2]/div/div/div/p[2]/button")
    add_tocart = LocatorStrategy.locator_by_name("Submit")

    def item_search(self):
        self.enter_text(ItemDetails.search_field, text=self.data['item'])
        self.click(ItemDetails.search_button)

    def product_details(self):
        self.time_sleep(config.sleep_time)
        self.actions(move1=ItemDetails.products, move2=ItemDetails.more_options)
        select = self.select_option_from_drop_down(ItemDetails.select_size)
        select.select_by_index(1)
        self.click(ItemDetails.change_color)
        self.verify_exact_text(ItemDetails.datasheet_properties, validatetext=self.data['datasheet_properties'])
        self.verify_exact_text(ItemDetails.dress_name,validatetext=self.data['dress_name'])


    def product_review_form(self):
        self.click(ItemDetails.write_review)
        self.enter_text(ItemDetails.review_title, text=self.data['review_title'])
        self.enter_text(ItemDetails.comment, text=self.data['comment'])
        self.click(ItemDetails.send_button)
        self.time_sleep(config.sleep_time)
        self.click(ItemDetails.comment_ok)


    def add_item_to_cart(self):
        self.click(ItemDetails.add_tocart)



