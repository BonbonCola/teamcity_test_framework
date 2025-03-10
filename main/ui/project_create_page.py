from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.ui.base_create_page import BaseCreatePage


class ProjectCreatePage(BaseCreatePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_project_name = (By.ID, "projectName")
        self.input_buildtype_name = (By.ID, "buildTypeName")

    @classmethod
    def open(cls, driver, project_id):
        show_mode = "createProjectMenu"
        driver.get(f"{Config().properties.servers.dev.internal_base_url}/admin/createObjectMenu.html?projectId={project_id}&showMode={show_mode}")
        return cls(driver)

    def create_form(self, repository_url):
        super().base_create_form(repository_url)

    def setup_project(self, project_name, buildtype_name):
        self.type(self.input_project_name, project_name)
        self.type(self.input_buildtype_name, buildtype_name)
        self.click(self.button_proceed)
