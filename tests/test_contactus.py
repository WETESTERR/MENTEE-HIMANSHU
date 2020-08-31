import allure

from page_objects.contact_page import Contact

@allure.feature("Contact Customer Support")
class TestContactUs:

    @allure.story("Fill Customer Service Form")
    def test_contactus_page(self,driver):
        c = Contact(driver)
        c.contact_us_form()
