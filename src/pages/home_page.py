from selenium.webdriver.common.by import By

from src.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.brand_name = driver.find_element(By.XPATH, Locators.page_logo)


    def get_text(self):
        return self.brand_name.text