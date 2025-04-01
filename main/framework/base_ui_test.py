from selenium import webdriver

from main.api.configs.config import Config
from main.api.specs.specifications import Specifications
from main.framework.base_test import BaseTest


class BaseUiTest(BaseTest):
    def setup_method(self): #настройка Selenium WebDriver в selenoid перед каждым тестом
        super().setup_method()
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "chrome")  # Явно указываем браузер
        options.set_capability("browserVersion", "91.0")  # Указываем версию!
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument(f"--window-size={Config().properties.browsers.browser_size}")

        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableLog": True
        })

        self.driver = webdriver.Remote(
            command_executor=Config().properties.servers.dev.selenoid_url,
            options=options
        )
        """ Подключает API-сессию ко всем тестам """
        self.specifications = Specifications()

    def teardown_method(self): #Закрытие браузера после теста
        super().teardown_method()
        if self.driver:
            self.driver.quit()