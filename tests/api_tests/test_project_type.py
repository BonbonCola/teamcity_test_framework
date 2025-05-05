from copy import copy

import pytest
import allure

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.api.requests.endpoints import Endpoint
from tests.conftest import generate_test_child_project, generate_test_project, generate_test_user, \
    generate_test_copy_project


@pytest.mark.regression
@pytest.mark.usefixtures("per_project_permissions")
class TestProject():

    @pytest.mark.positive
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User creates a project type successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_project(self, test_data, specifications):
        """User should be able to create project"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project by user"):
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            new_project = project_request.create(test_data.project.model_dump())
        with allure.step("Check project was created successfully with correct data"):
            created_project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            created_project = created_project_request.read(f'id:{test_data.project.id}')
            assert created_project.json()['id'] == test_data.project.id,  f"Ошибка: {created_project['id']} != {test_data.project.id}"

    @pytest.mark.positive
    @pytest.mark.roles
    @allure.feature("Project Management")
    @allure.story("User creates a project with parent project successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_project_with_parent_project(self, test_data, specifications):
        """User should be able to create project with parent project"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create a parent project by user"):
            parent_project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            parent_project_type = parent_project_request.create(test_data.project.model_dump())
        with allure.step("Create a child project by user"):
            child_project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            child_project = child_project_request.create(test_data.child_project.model_dump())
        with allure.step("Check child project was created successfully with correct data"):
            created_child_project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            created_child_project = created_child_project_request.read(f'id:{test_data.child_project.id}')
            assert created_child_project.json()['parentProjectId'] == test_data.project.id , f"Ошибка: {created_child_project['parentProjectId']} != {test_data.project.id}"
    
    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User cannot create two projects with the same ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_two_projects_with_same_id(self, test_data, specifications):
        """User cannot create two projects with the same ID"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project 1 by user"):
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            new_project = project_request.create(test_data.project.model_dump())
        with allure.step("Create project 2 by user with same id"):
            name = copy(test_data.project.name)
            test_data.project.name.replace(name, "another_name")
            second_project_request = UncheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            second_project = second_project_request.create(test_data.project.model_dump())
        with allure.step("Check project 2 was not created with bad request code"):
            assert second_project.status_code == 400, f"Ошибка: {second_project.status_code}"

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User cannot create two projects with the same name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_two_projects_with_same_name(self, test_data, specifications):
        """User cannot create two projects with the same name"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project 1 by user"):
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            new_project = project_request.create(test_data.project.model_dump())
        with allure.step("Create project 2 by user with same name"):
            id = test_data.project.id
            test_data.project.id.replace(id, "another_id")
            second_project_request = UncheckedRequest(specifications.authSpec(test_data.user),
                                                      Endpoint.PROJECTS.url)
            second_project = second_project_request.create(test_data.project.model_dump())
        with allure.step("Check project 2 was not created with bad request code"):
            assert second_project.status_code == 400, f"Ошибка: {second_project.status_code}"

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User cannot create project with empty name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_project_with_empty_name(self, test_data, specifications):
        """User cannot create project with empty name"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project by user with empty name"):
            project_request = UncheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            project = project_request.create(test_data.project.model_dump(exclude={"name"}))
        with allure.step("Check project was not created with bad request code"):
            assert project.status_code == 400, f"Ошибка: {project.status_code}"

    @pytest.mark.positive
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User can create project with empty ID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_project_with_empty_id(self, test_data, specifications):
        """User cannot create project with empty ID"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project by user with empty id"):
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            print(f'{test_data.project.model_dump(exclude={"id"})}')
            project = project_request.create(test_data.project.model_dump(exclude={"id"}))
        with allure.step("Check project was created with id == name"):
            assert project.json()['id'].lower() == test_data.project.name.replace(" ", "").replace("-", ""), f"Ошибка: id не совпадает!"

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User cannot create project without permission")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_creates_project_without_permission(self, test_data, specifications):
        """User cannot create project without permission"""
        with allure.step("Create admin user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            admin_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create user without permission"):
            new_user_without_permission_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user_without_permission = generate_test_user("PROJECT_VIEWER", "g") #TODO: сделать тут тоже enum и нормально обращаться к этим параметрам
            new_user_without_permission_created = new_user_without_permission_request.create(new_user_without_permission.model_dump())
        with allure.step("Create project by user"):
            project_request = UncheckedRequest(specifications.authSpec(new_user_without_permission), Endpoint.PROJECTS.url)
            project = project_request.create(test_data.project.model_dump())
        with allure.step("Check  project was not created with bad request code"):
            assert project.status_code == 403, f"Ошибка: {project.status_code}"

    @pytest.mark.negative
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("Admin user cannot create project in another user's project area")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_admin_user_creates_project_in_another_user_project_area(self, test_data, specifications):
        """Admin user cannot create project in another user's project area"""
        with allure.step("Create project area 1"):
            project_request = CheckedRequest(specifications.superUserSpec(), Endpoint.PROJECTS.url)
            project_request.create(test_data.project.model_dump())
        with allure.step("Create project area 2"):
            #TODO: сделать фабрику и не использовать так
            project_2 = generate_test_project()
            project_2_request = CheckedRequest(specifications.superUserSpec(), Endpoint.PROJECTS.url)
            project_2_request.create(project_2.model_dump())
        with allure.step("Create admin user for project area 2"):
            admin_user_2 = generate_test_user("PROJECT_ADMIN", f"p:{project_2.id}")
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            user_request.create(admin_user_2.model_dump())
        with allure.step("Create child project in project area 1 by admin user for project area 2"):
            child_project_1 = generate_test_child_project(test_data.project)
            child_project_request = UncheckedRequest(specifications.authSpec(admin_user_2), Endpoint.PROJECTS.url)
            child_project_created = child_project_request.create(child_project_1.model_dump())
        with allure.step("Check child project was not created with bad request code"):
            assert child_project_created.status_code == 403, f"Ошибка: {child_project_created.status_code}"


    @pytest.mark.positive
    @pytest.mark.crud
    @allure.feature("Project Management")
    @allure.story("User can copy project")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_copy_project(self, test_data, specifications):
        """User should be able to copy project"""
        with allure.step("Create user"):
            user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url)
            new_user = user_request.create(test_data.user.model_dump())
        with allure.step("Create project by user"):
            project_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            new_project = project_request.create(test_data.project.model_dump())
        with allure.step("Copy project"):
            #TODO: сделать фабрику и не использовать так
            project_copy = generate_test_copy_project(source_project=test_data.project)
            project_copy_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            print(f'COPY:{project_copy.model_dump()}')
            project_copy_request.create(project_copy.model_dump())
        with allure.step("Check project was copied successfully with correct data"):
            project_copy_created_request = CheckedRequest(specifications.authSpec(test_data.user), Endpoint.PROJECTS.url)
            project_copy_created = project_copy_created_request.read(f'id:{project_copy.id}')
            assert project_copy_created.json()['id'] == project_copy.id,  f"Ошибка: {project_copy_created['id']} != {test_data.project.id}"