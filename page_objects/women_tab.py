from page_objects.common import Common
from utilities.locator_strategy import LocatorStrategy


class Womentab(Common):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    women_tab = LocatorStrategy.locator_by_xpath("//div[@id='block_top_menu']/ul/li[1]")
    left_slider = LocatorStrategy.locator_by_css_selector("#layered_price_slider > a:nth-child(2)")


    def slider_range(self):
        self.click(Womentab.women_tab)
        self.drag_drop_offset(Womentab.left_slider,150,100)
