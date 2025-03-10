from main.api.configs.config import Config
from main.ui.base_page import BasePage

from selenium.webdriver.common.by import By


class ProjectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title_project_name = (By.CSS_SELECTOR, "span.ProjectPageHeader__title--ih")

    @classmethod
    def open(cls, driver, project_id):
        driver.get(
            f"{Config().properties.servers.dev.internal_base_url}/project/{project_id}")
        return cls(driver)

    def get_title_project_name(self):
        title = self.find(self.title_project_name)
        return title.text

