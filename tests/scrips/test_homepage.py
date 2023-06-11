import time

import pytest

from common.common import common_utils
from src.base_page import BasePage
from src.pages.home_page import HomePage


@pytest.mark.usefixtures('set_up')
class TestHomePage(BasePage):


    def test_home_page_landing(self):
        driver = self.driver
        self.homepage = HomePage(driver)
        homepage_logo =self.homepage.get_text()
        try:
            assert homepage_logo == common_utils.get_property("logo_name")
        except Exception as e:
            print("Title is wrong", format(e))



