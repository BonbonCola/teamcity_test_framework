import pytest
import allure

from tests.factories.generators import GenerateTest
from tests.helpers.test_data_storage import TestDataStorage

import logging
logger = logging.getLogger(__name__)

@pytest.fixture
def project_factory(specifications): # генерирует тестовый проект и не создает чере апи, тк в шагах тестов пока мы проверяем именно создание, удаляет их после завершения теста
    def project_builder(parent_project=None, source_project=None):
        with allure.step(f"Generate project with parent_project: {parent_project}, source_project: {source_project}"):
            project = GenerateTest.generate_test_project_full(parent_project, source_project)
            return project
    yield project_builder
    TestDataStorage().delete_created_entities()