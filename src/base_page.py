
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from common.common import common_utils


class BasePage:

    @pytest.fixture(autouse=True)
    def set_up(self):

        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)

        self.driver.get("https://demo.realworld.io/#/")
        self.driver.maximize_window()

        yield self.driver

        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()


