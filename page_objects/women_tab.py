import config
from page_objects.common import Common
from utilities.locator_strategy import LocatorStrategy


class Womentab(Common):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    women_tab = LocatorStrategy.locator_by_xpath("//div[@id='block_top_menu']/ul/li[1]")
    left_slider = LocatorStrategy.locator_by_xpath("//a[contains(@class,'ui-slider-handle')][1]")
    right_slider = LocatorStrategy.locator_by_xpath("//a[contains(@class,'ui-slider-handle')][2]")
    size_checkbox = LocatorStrategy.locator_by_id("layered_id_attribute_group_3")


    def slider_range(self):
        self.click(Womentab.women_tab)
        self.time_sleep(config.sleep_time)
        self.click(Womentab.size_checkbox)
        self.time_sleep(config.sleep_time)
        self.drag_drop_offset(Womentab.left_slider,50,0)
        self.drag_drop_offset(Womentab.right_slider, -70, 0)

