import allure
import pytest

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.endpoints import Endpoint
from main.ui.login_page import LoginPage
from main.ui.project_create_page import ProjectCreatePage
from main.ui.project_page import ProjectPage
from main.ui.projects_page import ProjectsPage
import time

@pytest.mark.regression
class TestCreateProject():

    @pytest.mark.positive
    def test_user_creates_project(self, test_data, specifications, driver):
        """User should be able to create project"""
        #подготовка окружения
        with allure.step("Login as user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(test_data.user.model_dump())
            login_page = LoginPage.open(driver)
            login_page.login(test_data.user)
        #взаимодействие с UI
        with allure.step("Open `Create Project Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_project_page  = ProjectCreatePage.open(driver = driver, project_id="_Root")
            time.sleep(10)
        with allure.step("Send all project parameters (repository URL)"):
            create_project_page.create_form("https://github.com/BonbonCola/test_teamcity")
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Fix Project Name and Build Type name values"):
            create_project_page.setup_project(test_data.project.name, test_data.buildtype.name)
        with allure.step("Click `Proceed`"):
            pass
        #проверка состояния API
        #(корректность отправки данных с UI на API)
        with allure.step("Check that all entities (project, build type) was successfully created with correct data on API level"):
            project_request = CheckedRequest(specifications.superUserSpec(), Endpoint.PROJECTS.url)
            created_project = project_request.read(f'name:{test_data.project.name}')
            assert created_project.json()["name"] == test_data.project.name, f"Ошибка: нет {test_data.project.name}"
        #проверка состояния UI
        #(корректность считывания данных и отображение данных на UI)
        with allure.step("Check that project is visible on Project Page (http://localhost:8111/project/{project_id})"):
            project_page = ProjectPage.open(driver=driver, project_id=created_project.json()["id"])
            assert project_page.get_title_project_name() == test_data.project.name, f"Ошибка: нет {test_data.project.name}"
        with allure.step("Check that project is visible on Projects Page (http://localhost:8111/favorite/projects)"):
            projects_page = ProjectsPage.open(driver=driver)
            projects = projects_page.get_projects()
            projects_names = []
            for p in projects:
                projects_names.append(p.get_name())
            assert test_data.project.name in projects_names, f"Ошибка: {test_data.project.name} нет в списке"

    @pytest.mark.negative
    def test_user_creates_project_without_name(self, test_data, specifications, driver):
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