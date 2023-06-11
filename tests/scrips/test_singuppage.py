import time

import pytest

from src.base_page import BasePage
from src.pages.singup_page import SignUpPage


@pytest.mark.usefixtures('set_up')
class TestSignupPage(BasePage):

    def test_singup_valid(self):
        driver = self.driver
        self.singup_page = SignUpPage(driver)
        self.singup_page.singup_new_user()


    def test_singin_valid(self):
        driver = self.driver
        self.singup_page = SignUpPage(driver)
        self.singup_page.click_on_singin()



    def test_article_creation(self):
        driver = self.driver
        self.singup_page = SignUpPage(driver)
        self.singup_page.create_article()




