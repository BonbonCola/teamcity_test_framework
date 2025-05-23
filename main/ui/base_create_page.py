from selenium.webdriver.common.by import By
import time

from main.ui.base_page import BasePage


class BaseCreatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(15)
        self.input_repository_url = (By.ID, "url")
        self.button_proceed = (By.CSS_SELECTOR, ".submitButton")
        self.message_connection_successful = (By.CLASS_NAME, "connectionSuccessful")

    def base_create_form(self, repository_url):
        time.sleep(15)
        self.type(self.input_repository_url, repository_url)
        self.click(self.button_proceed)


