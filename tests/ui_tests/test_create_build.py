import allure
import pytest

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.endpoints import Endpoint
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.framework.base_ui_test import BaseUiTest
from main.ui.build_create_page import BuildCreatePage
from main.ui.build_page import BuildPage
from main.ui.login_page import LoginPage

@pytest.mark.regression
class TestCreateBuild(BaseUiTest):

    def test_user_creates_build(self):
        """User should be able to create build"""
        # подготовка окружения
        with allure.step("Create user and project"):
            user_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(self.test_data.user.model_dump())
            project_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.PROJECTS.url)
            project_request.create(self.test_data.project.model_dump())
        with allure.step("Login as user"):
            login_page = LoginPage.open(self.driver)
            login_page.login(self.test_data.user)
        # взаимодействие с UI
        with allure.step("Open `Create Build Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_build_page = BuildCreatePage.open(driver = self.driver, project_id=self.test_data.project.id)
        with allure.step("Send all build parameters (repository URL)"):
            create_build_page.create_form("https://github.com/BonbonCola/test_teamcity")
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Fix Build Type name value"):
            create_build_page.setup_build(self.test_data.buildtype.name)
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Check that build type was successfully created with correct data on API level"):
            build_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            created_build = build_request.read(f'name:{self.test_data.buildtype.name}')
            assert created_build.json()["name"] == self.test_data.buildtype.name, f'Ошибка, {created_build.json()["name"]}  != {self.test_data.buildtype.name}'
        with allure.step("Check that build is visible on build page (http://localhost:8111/buildConfiguration/{build_id})"):
            build_page = BuildPage.open(self.driver, self.test_data.project.id, self.test_data.buildtype.name)
            assert build_page.get_title_build_name() == self.test_data.buildtype.name, f'Ошибка, {build_page.get_title_build_name()}  != {self.test_data.buildtype.name}'

    def test_user_creates_build_without_name(self):
        """User should not be able to create build without a name"""
        # подготовка окружения
        with allure.step("Create user and project"):
            user_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(self.test_data.user.model_dump())
            project_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.PROJECTS.url)
            project_request.create(self.test_data.project.model_dump())
        with allure.step("Login as user"):
            login_page = LoginPage.open(self.driver)
            login_page.login(self.test_data.user)
            # взаимодействие с UI
        with allure.step("Open `Create Build Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_build_page = BuildCreatePage.open(driver=self.driver, project_id=self.test_data.project.id)
        with allure.step("Send all build parameters (repository URL)"):
            create_build_page.base_create_form("https://github.com/BonbonCola/test_teamcity")
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Remove Build Type name value"):
            create_build_page.setup_build_without_name()
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Check that build  was not created and error was shown"):
            assert "Build configuration name must not be empty" in create_build_page.get_error_build_type_text(), 'Текст ошибки не совпадает'
        with allure.step(
            "Check that build  was not created on API level"):
            build_request = UncheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            created_build = build_request.read(f'name:{self.test_data.buildtype.name}')
            assert created_build.status_code == 404, f"Ошибка: {created_build.status_code}"

