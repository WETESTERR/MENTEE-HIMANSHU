from page_objects.login import Login




class TestLogin:

    def test_login(self,driver,email,password):

        l = Login(driver)

        l.navigate_to_login_page()
        l.login(email,password)
        l.logout()





