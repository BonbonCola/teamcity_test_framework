from selenium.webdriver.common.by import By

from main.api.configs.config import Config
from main.ui.base_page import BasePage
from main.ui.project_element import ProjectElement


class ProjectsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.projects_list = (By.CSS_SELECTOR, "div[class*='Subproject__container']")

    @classmethod
    def open(cls, driver):
        driver.get(f"{Config().properties.servers.dev.internal_base_url}/favorite/projects")
        return cls(driver)

    def get_projects(self):
        elements = self.find_all(self.projects_list)
        projects = []
        for e in elements:
            project = ProjectElement(e)
            projects.append(project)
        return projects
