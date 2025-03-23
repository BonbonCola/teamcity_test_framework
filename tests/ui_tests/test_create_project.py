import allure

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.endpoints import Endpoint
from main.framework.base_ui_test import BaseUiTest
from main.ui.login_page import LoginPage
from main.ui.project_create_page import ProjectCreatePage
from main.ui.project_page import ProjectPage
from main.ui.projects_page import ProjectsPage


class TestCreateProject(BaseUiTest):

    def test_user_creates_project(self):
        """User should be able to create project"""
        #подготовка окружения
        with allure.step("Login as user"):
            user_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(self.test_data.user.model_dump())
            login_page = LoginPage.open(self.driver)
            login_page.login(self.test_data.user)
        #взаимодействие с UI
        with allure.step("Open `Create Project Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_project_page  = ProjectCreatePage.open(driver = self.driver, project_id="_Root")
        with allure.step("Send all project parameters (repository URL)"):
            create_project_page.create_form("https://github.com/BonbonCola/test_teamcity")
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Fix Project Name and Build Type name values"):
            create_project_page.setup_project(self.test_data.project.project_name, self.test_data.buildtype.project_name)
        with allure.step("Click `Proceed`"):
            pass
        #проверка состояния API
        #(корректность отправки данных с UI на API)
        with allure.step("Check that all entities (project, build type) was successfully created with correct data on API level"):
            project_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.PROJECTS.url)
            created_project = project_request.read(f'name:{self.test_data.project.project_name}')
            assert created_project.json()["name"] == self.test_data.project.project_name, f"Ошибка: нет {self.test_data.project.project_name}"
        #проверка состояния UI
        #(корректность считывания данных и отображение данных на UI)
        with allure.step("Check that project is visible on Project Page (http://localhost:8111/project/{project_id})"):
            project_page = ProjectPage.open(driver=self.driver, project_id=created_project.json()["id"])
            assert project_page.get_title_project_name() == self.test_data.project.project_name, f"Ошибка: нет {self.test_data.project.project_name}"
        with allure.step("Check that project is visible on Projects Page (http://localhost:8111/favorite/projects)"):
            projects_page = ProjectsPage.open(driver=self.driver)
            projects = projects_page.get_projects()
            projects_names = []
            for p in projects:
                projects_names.append(p.get_name())
            assert self.test_data.project.project_name in projects_names, f"Ошибка: {self.test_data.project.project_name} нет в списке"

    def test_user_creates_project_without_name(self):
        with allure.step("Login as user"):
            pass
        with allure.step("Check number of projects"):
            pass
        with allure.step("Open `Create Project Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            pass
        with allure.step("Send all project parameters (repository URL)"):
            pass
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Set Project Name"):
            pass
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Check that number of projects did not change"):
            pass
        with allure.step("Check that error appears `Project name must not be empty`"):
            pass