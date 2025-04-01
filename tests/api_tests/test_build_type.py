import pytest
import allure

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.framework.base_api_test import BaseApiTest
from main.api.requests.endpoints import Endpoint


@pytest.mark.regression
class TestBuildType(BaseApiTest):

    @pytest.mark.positive
    @pytest.mark.crud
    @allure.feature("Build Type Management")
    @allure.story("User creates a build type successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_build_type(self):
        """User should be able to create build type"""
        with allure.step("Create user"):
            user_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(self.test_data.user.model_dump())
        with allure.step("Create project by user"):
            project_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.PROJECTS.url)
            new_project  = project_request.create(self.test_data.project.model_dump())
        with allure.step("Create buildType for project by user"):
            buildtype_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            print(f'ОТПРАВЛЯЕМ:')
            print(self.test_data.buildtype.model_dump())
            new_buildtype = buildtype_request.create(self.test_data.buildtype.model_dump())
        with allure.step("Check buildType was created successfully with correct data"):
            created_buildtype_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            created_buildtype = created_buildtype_request.read(f'id:{self.test_data.buildtype.id}')
            assert created_buildtype.json()["id"] == self.test_data.buildtype.id,  f"Ошибка: {created_buildtype["id"]} != {self.test_data.buildtype.id}"

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Build Type Management")
    @allure.story("User cannot create two build types with the same ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_two_build_types_with_same_id(self):
        """User should not be able to create two build types with the same ID"""
        with allure.step("Create user"):
            user_request = CheckedRequest(self.specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(self.test_data.user.model_dump())
        with allure.step("Create project by user"):
            project_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.PROJECTS.url)
            new_project = project_request.create(self.test_data.project.model_dump())
        with allure.step("Create buildType1 for project by user"):
            buildtype_request = CheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            first_buildtype = buildtype_request.create(self.test_data.buildtype.model_dump())
        with allure.step("Create buildType2 with same id as buildType1 for project by user"):
            buildtype_request = UncheckedRequest(self.specifications.authSpec(self.test_data.user), Endpoint.BUILD_TYPES.url)
            second_buildtype = buildtype_request.create(self.test_data.buildtype.model_dump())
        with allure.step("Check buildType2 was not created with bad request code"):
            assert second_buildtype.status_code == 400, f"Ошибка: {second_buildtype.status_code}"

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
