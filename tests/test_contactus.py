from page_objects.contact_page import Contact


class TestContactUs:


    def test_contactus_page(self,driver):
        c = Contact(driver)
        c.contact_us_form()
