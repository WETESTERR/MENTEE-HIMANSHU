from page_objects.women_tab import Womentab


class TestSliderRange:


    def test_slider_range_functionality(self,driver):
        w = Womentab(driver)
        w.slider_range()

