import requests
import pytest
import allure

from main.api.crud_requests.checked_request import CheckedRequest
from main.api.models.api_models import BuildType
from main.api.models.user_model import User
from main.api.specs.specifications import Specifications
from main.framework.base_api_test import BaseApiTest
from main.framework.logger import logger
from main.api.crud_requests.endpoints import Endpoint
from tests.conftest import generate_test_user, generate_test_project, generate_test_build_type


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
            user = generate_test_user("PROJECT_ADMIN", "g")
            user_request = CheckedRequest(Specifications().superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(user.model_dump())
        with allure.step("Create project by user"):
            project = generate_test_project()
            project_request = CheckedRequest(Specifications().authSpec(user), Endpoint.PROJECTS.url)
            new_project  = project_request.create(project.model_dump())
            project.locator = None
        with allure.step("Create buildType for project by user"):
            buildtype = generate_test_build_type(project)
            buildtype_request = CheckedRequest(Specifications().authSpec(user), Endpoint.BUILD_TYPES.url)
            new_buildtype = buildtype_request.create(buildtype.model_dump())
        with allure.step("Check buildType was created successfully with correct data"):
            created_buildtype_request = CheckedRequest(Specifications().authSpec(user), Endpoint.BUILD_TYPES.url)
            created_buildtype = created_buildtype_request.read(buildtype.id)
            assert created_buildtype.json()["id"] == buildtype.id,  f"Ошибка: {created_buildtype["id"]} != {buildtype.id}"

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
