import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(("http://automationpractice.com/index.php"))
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='login']").click()
driver.find_element_by_css_selector("input[id='email_create']").send_keys("hs002@gmail.com")
driver.find_element_by_xpath("//button[@id='SubmitCreate']").click()
print(driver.find_element_by_tag_name("h3").text)
#Form Filling
driver.switch_to.frame()
driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("Himanshu")
'''driver.find_element_by_id("customer_lastname").send_keys("Sethi")
driver.find_element_by_name("passwd").send_keys("abc123")
driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Himanshu")
driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Sethi")
driver.find_element_by_id("address1").send_keys("123,E Str")'''
