from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.api.models.user_model import User
from main.ui.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        #login_url = "/login.html"
        self.input_username = (By.ID, "username")
        self.input_password = (By.ID, "password")
        self.button_login = (By.CSS_SELECTOR, ".loginButton")

    @classmethod
    def open(cls, driver):
        """Открывает страницу логина и возвращает объект LoginPage"""
        driver.get(f"{Config().properties.servers.dev.internal_base_url}/login.html")
        return cls(driver)

    def login(self, user: User):
        self.type(self.input_username, user.username)
        self.type(self.input_password, user.password)
        self.click(self.button_login)