import allure
import pytest

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.endpoints import Endpoint
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.ui.build_create_page import BuildCreatePage
from main.ui.build_page import BuildPage
from main.ui.login_page import LoginPage
import time

@pytest.mark.regression
class TestCreateBuild():

    def test_user_creates_build(self, test_data, specifications, driver):
        """User should be able to create build"""
        # подготовка окружения
        with allure.step("Create user and project"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(test_data.user.model_dump())
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            project_request.create(test_data.project.model_dump())
        with allure.step("Login as user"):
            driver.delete_all_cookies()
            login_page = LoginPage.open(driver)
            driver.save_screenshot("teamcity_fail.png")
            login_page.login(test_data.user)
        # взаимодействие с UI
        with allure.step("Open `Create Build Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_build_page = BuildCreatePage.open(driver = driver, project_id=test_data.project.id)
            time.sleep(15)
        with allure.step("Send all build parameters (repository URL)"):
            driver.save_screenshot("teamcity_fail1.png")
            create_build_page.base_create_form("https://github.com/BonbonCola/test_teamcity")
        with allure.step("Click `Proceed`"):
            time.sleep(10)
            pass
        with allure.step("Fix Build Type name value"):
            create_build_page.setup_build(test_data.buildtype.name)
        with allure.step("Click `Proceed`"):
            pass
        with allure.step("Check that build type was successfully created with correct data on API level"):
            time.sleep(10)
            build_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.BUILD_TYPES.url)
            created_build = build_request.read(f'name:{test_data.buildtype.name}')
            assert created_build.json()["name"] == test_data.buildtype.name, f'Ошибка, {created_build.json()["name"]}  != {test_data.buildtype.name}'
        with allure.step("Check that build is visible on build page (http://localhost:8111/buildConfiguration/{build_id})"):
            build_page = BuildPage.open(driver, test_data.project.id, test_data.buildtype.name)
            assert build_page.get_title_build_name() == test_data.buildtype.name, f'Ошибка, {build_page.get_title_build_name()}  != {test_data.buildtype.name}'

    def test_user_creates_build_without_name(self, test_data, specifications, driver):
        """User should not be able to create build without a name"""
        # подготовка окружения
        with allure.step("Create user and project"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(test_data.user.model_dump())
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            project_request.create(test_data.project.model_dump())
        with allure.step("Login as user"):
            driver.delete_all_cookies()
            login_page = LoginPage.open(driver)
            login_page.login(test_data.user)
            # взаимодействие с UI
        with allure.step("Open `Create Build Page` (http://localhost:8111/admin/createObjectMenu.html)"):
            create_build_page = BuildCreatePage.open(driver=driver, project_id=test_data.project.id)
            time.sleep(15)
        with allure.step("Send all build parameters (repository URL)"):
            create_build_page.base_create_form("https://github.com/BonbonCola/test_teamcity")
            time.sleep(10)
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
            build_request = UncheckedRequest(specifications.authSpec(test_data.user), Endpoint.BUILD_TYPES.url)
            created_build = build_request.read(f'name:{test_data.buildtype.name}')
            assert created_build.status_code == 404, f"Ошибка: {created_build.status_code}"

