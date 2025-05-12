import pytest


@pytest.fixture
def user_factory(specifications):
    def user_builder(**kwargs):
        pass