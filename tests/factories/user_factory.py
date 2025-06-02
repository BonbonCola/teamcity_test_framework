import pytest
import allure

from main.api.requests.checked_crud_request import CheckedRequest
from main.api.requests.endpoints import Endpoint
from tests.factories.generators import GenerateTest
from tests.helpers.test_data_storage import TestDataStorage


@pytest.fixture
def user_factory(specifications): # генерирует тестового пользователя и создает его через апи для каждого теста, удаляет их после завершения теста
    def user_builder(role_id="PROJECT_ADMIN", scope_type="g"): #значение роли и скоупа по умолчанию
        with allure.step(f"Create user with role_id={role_id}, scope_type={scope_type}"):
            with allure.step("Generate user"):
                user = GenerateTest.generate_test_user(role_id, scope_type)
            with allure.step("Create user at backend"):
                user_request = CheckedRequest(specifications.superUserSpec(), Endpoint.USERS.url) #создаем пользователя на беке через апи
                new_user = user_request.create(user.model_dump())
        return user
    yield user_builder
    TestDataStorage().delete_created_entities()
