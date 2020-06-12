from page_objects.login import Login



class TestLogin:

    def test_login(self,driver,email,password):
        l = Login(driver)

        l.loginbutton().click()
        l.loginemail().sendkeys(email)
        l.loginpwd().sendkeys(password)
        l.submitbutton().click()
        l.logoutbutton().click()
