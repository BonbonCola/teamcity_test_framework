from tests.conftest import TestData


class BaseTest:
    def setup_method(self):
        self.test_data = TestData()