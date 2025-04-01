from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.ui.base_create_page import BaseCreatePage
import time

class BuildCreatePage(BaseCreatePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_buildtype_name = (By.ID, "buildTypeName")
        self.error_build_type_name = (By.ID, "error_buildTypeName")

    @classmethod
    def open(cls, driver, project_id):
        show_mode = "createBuildTypeMenu"
        driver.get(f'{Config().properties.servers.dev.internal_base_url}/admin/createObjectMenu.html?projectId={project_id}&showMode={show_mode}')
        return cls(driver)

    def create_form(self, repository_url):
        super().base_create_form(repository_url)

    def setup_build(self, buildtype_name):
        time.sleep(15)
        self.type(self.input_buildtype_name, buildtype_name)
        self.click(self.button_proceed)

    def setup_build_without_name(self):
        self.type(self.input_buildtype_name, "")
        self.click(self.button_proceed)

    def get_error_build_type_text(self):
        error = self.find(self.error_build_type_name)
        return error.text
