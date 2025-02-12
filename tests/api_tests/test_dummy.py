import requests
import pytest
import allure
from main.framework.base_api_test import BaseApiTest
from main.framework.logger import logger

class TestDummy(BaseApiTest):

    def test_get_projects(self):
        with allure.step("Отправляем GET-запрос на список проектов"):
            response = self.session.get(f"http://{self.base_url}/app/rest/projects")
            allure.attach(response.text, name="API Response", attachment_type=allure.attachment_type.JSON)
        logger.info(f"Ответ API: {response.json()}")
        with allure.step("Получаем список проектов"):
            pass
        assert response.status_code == 200, f"Ошибка: {response.status_code}"

@pytest.mark.regression
class TestBuildType:

    @pytest.mark.positive
    @pytest.mark.crud
    @allure.feature("Build Type Management")
    @allure.story("User creates a build type successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_build_type(self):
        """User should be able to create build type"""
        with allure.step("Create user"):
            pass
        with allure.step("Create project by user"):
            pass
        with allure.step("Create buildType for project by user"):
            pass
        with allure.step("Check buildType was created successfully with correct data"):
            pass

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Build Type Management")
    @allure.story("User cannot create two build types with the same ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_two_build_types_with_same_id(self):
        """User should not be able to create two build types with the same ID"""
        with allure.step("Create user"):
            pass
        with allure.step("Create project by user"):
            pass
        with allure.step("Create buildType1 for project by user"):
            pass
        with allure.step("Create buildType2 with same id as buildType1 for project by user"):
            pass
        with allure.step("Check buildType2 was not created with bad request code"):
            pass

    @pytest.mark.positive
    @pytest.mark.roles
    @allure.feature("Roles & Permissions")
    @allure.story("Project admin creates a build type successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_project_admin_creates_build_type(self):
        """Project admin should be able to create build type for their project"""
        with allure.step("Create user"):
            pass
        with allure.step("Create project"):
            pass
        with allure.step("Grant user PROJECT_ADMIN role in project"):
            pass
        with allure.step("Create buildType for project by user (PROJECT_ADMIN)"):
            pass
        with allure.step("Check buildType was created successfully"):
            pass

    @pytest.mark.negative
    @pytest.mark.roles
    @allure.feature("Roles & Permissions")
    @allure.story("Project admin cannot create a build type for another user's project")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_project_admin_creates_build_type_for_another_user_project(self):
        """Project admin should not be able to create build type for not their project"""
        with allure.step("Create user1"):
            pass
        with allure.step("Create project1"):
            pass
        with allure.step("Grant user1 PROJECT_ADMIN role in project1"):
            pass
        with allure.step("Create user2"):
            pass
        with allure.step("Create project2"):
            pass
        with allure.step("Grant user2 PROJECT_ADMIN role in project2"):
            pass
        with allure.step("Create buildType for project1 by user2"):
            pass
        with allure.step("Check buildType was not created with forbidden code"):
            pass
