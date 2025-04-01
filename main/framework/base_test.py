from tests.conftest import TestData, TestDataStorage


class BaseTest:
    def setup_method(self):
        """Создание тестовых данных перед тестами"""
        self.test_data = TestData()

    def teardown_method(self):
        """Удаление созданных тестовых данных после тестов"""
        TestDataStorage().delete_created_entities()