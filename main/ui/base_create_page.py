from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.ui.base_page import BasePage


class BaseCreatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_repository_url = (By.ID, "url")
        self.button_proceed = (By.CSS_SELECTOR, ".submitButton")

    def base_create_form(self, repository_url):
        self.type(self.input_repository_url, repository_url)
        self.click(self.button_proceed)


