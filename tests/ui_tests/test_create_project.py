import pytest
import allure

from main.api.crud_requests.checked_request import CheckedRequest
from main.api.crud_requests.endpoints import Endpoint
from main.framework.base_ui_test import BaseUiTest
from main.ui.login_page import LoginPage


class TestCreateProject(BaseUiTest):

    def test_simple_test(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

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
            pass
        with allure.step("Send all project parameters (repository URL)"):
            pass
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Fix Project Name and Build Type name values"):
            pass
        with allure.step("Click `Proceed`"):
            pass
        #проверка состояния API
        #(корректность отправки данных с UI на API)
        with allure.step("Check that all entities (project, build type) was successfully created with correct data on API level"):
            pass
        #проверка состояния UI
        #(корректность считывания данных и отображение данных на UI)
        with allure.step("Check that project is visible on Projects Page (http://localhost:8111/favorite/projects)"):
            pass

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