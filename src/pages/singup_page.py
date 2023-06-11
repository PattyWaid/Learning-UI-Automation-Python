import time
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.common import common_utils
from src.locators import Locators


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.explicit_wait = WebDriverWait(self.driver, 30)
        self.uuid=str(uuid.uuid4())[:6]


    def click_on_singup(self):
        self.signup_link = self.driver.find_element(By.XPATH, Locators.singup_link)
        self.signup_link.click()

    def click_on_singin(self):
        self.singin_link = self.driver.find_element(By.XPATH, Locators.singin_link)
        self.singin_link.click()
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.signin_email_input)))
        self.driver.find_element(By.XPATH, Locators.signin_email_input).send_keys(common_utils.get_property("email"))
        self.driver.find_element(By.XPATH, Locators.signin_password_input).send_keys(common_utils.get_property("password"))
        self.driver.find_element(By.XPATH, Locators.singin_button).click()
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.signin_home_page)))


    def singup_new_user(self):
        self.click_on_singup()
        self.username_field = self.driver.find_element(By.XPATH, Locators.username_input)
        self.email_field = self.driver.find_element(By.XPATH, Locators.email_input)
        self.password_field = self.driver.find_element(By.XPATH, Locators.password_input)
        self.signin_button = self.driver.find_element(By.XPATH, Locators.signup_button)
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.signup_button)))
        username=common_utils.get_property("username")+f"_{self.uuid}"
        common_utils.set_property("username", username)
        email=common_utils.get_property("email").replace("@",f"_{self.uuid}@")
        common_utils.set_property("email", email)
        self.username_field.send_keys(username)
        self.email_field.send_keys(email)
        self.password_field.send_keys(common_utils.get_property("password"))
        self.signin_button.click()
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.signin_home_page)))



    def create_article(self):
        self.click_on_singin()
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.signin_home_page)))
        self.driver.find_element(By.XPATH, Locators.new_article_link).click()
        self.explicit_wait.until(EC.visibility_of_element_located((By.XPATH, Locators.article_title_input)))
        self.driver.find_element(By.XPATH, Locators.article_title_input).send_keys(common_utils.get_property("article_title"))
        self.driver.find_element(By.XPATH, Locators.article_about_input).send_keys(
            common_utils.get_property("article_about"))
        self.driver.find_element(By.XPATH, Locators.article_description_input).send_keys(
            common_utils.get_property("article_description"))
        self.driver.find_element(By.XPATH, Locators.article_tags_input).send_keys(
            common_utils.get_property("article_tags"))
        self.driver.find_element(By.XPATH, Locators.publish_article_button).click()




