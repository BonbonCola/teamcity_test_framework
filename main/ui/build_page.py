from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.ui.base_page import BasePage


class BuildPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = (By.XPATH, "//h1[contains(@class, 'BuildTypePageHeader__heading')]/span")

    @classmethod
    def open(cls, driver, project_id, build_name):
        driver.get(f'{Config().properties.servers.dev.internal_base_url}/buildConfiguration/{project_id}_{build_name}')
        return cls(driver)

    def get_title_build_name(self):
        title = self.find(self.header)
        return title.text