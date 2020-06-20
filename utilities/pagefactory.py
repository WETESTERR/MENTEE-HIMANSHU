from selenium.webdriver.common.by import By


class PageFactory:

    Type_Of_locators={
        "css":By.CSS_SELECTOR,
        "id":By.ID,
        "x-path":By.XPATH,
        "name":By.NAME,
        "link_text":By.LINK_TEXT,
        "partial_link_text":By.PARTIAL_LINK_TEXT,
        "tag_name":By.TAG_NAME,
        "class_name":By.CLASS_NAME
    }

