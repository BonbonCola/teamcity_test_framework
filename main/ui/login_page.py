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
        self.input_admin_username = (By.ID, "input_teamcityUsername")
        self.input_admin_password = (By.ID, "password1")
        self.input_confirm_password = (By.ID, "retypedPassword")

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

    def create_admin_user(self):
        self.type(self.input_admin_username, "test")
        self.type(self.input_admin_password, "test")
        self.type(self.input_confirm_password, "test")
        self.click(self.button_login)