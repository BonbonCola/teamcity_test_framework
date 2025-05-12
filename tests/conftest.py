import sys
import os
from copy import copy

import pytest

from selenium import webdriver
from main.api.configs.config import Config

from main.api.models.server_auth_settings import ServerAuthSettings
from main.api.requests.endpoints import Endpoint
from main.api.requests.server_auth_settings_request import ServerAuthSettingRequest
from main.api.specs.specifications import Specifications
from tests.factories.generators import generate_test_project, generate_test_user, generate_test_build_type, \
    generate_test_child_project
from tests.helpers.test_data_storage import TestDataStorage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class TestData():
    def __init__(self):
        self.user = generate_test_user()
        self.project = generate_test_project()
        self.project.locator
        self.buildtype = generate_test_build_type(self.project)
        self.child_project = generate_test_child_project(self.project)

@pytest.fixture(scope="function") # генерирует тестовые данные для каждого теста и удаляем их после завершения теста
def test_data():
    test_data = TestData()
    yield test_data
    TestDataStorage().delete_created_entities()

@pytest.fixture(scope="function")
def specifications():
    """ Подключает API-сессию ко всем тестам """
    specifications = Specifications()
    yield specifications

@pytest.fixture(scope="session")
def per_project_permissions():
    specifications = Specifications()
    # Получаем текущие настройки per_project_permissions
    permissions_request = ServerAuthSettingRequest(specifications.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
    permissions_response = permissions_request.read()
    permissions_response_to_json = permissions_response.json()
    per_project_permissions = ServerAuthSettings(**permissions_response_to_json)
    # Обновляем значение per_project_permissions на true
    new_per_project_permissions = copy(per_project_permissions)
    new_per_project_permissions.perProjectPermissions = True
    update_permissions_request = ServerAuthSettingRequest(specifications.superUserSpec(),
                                                          Endpoint.AUTH_SETTINGS.url)
    update_permissions_request.update(new_per_project_permissions.model_dump())
    yield
    # Возвращаем настройке perProjectPermissions исходное значение
    permissions_request = ServerAuthSettingRequest(specifications.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
    permissions_response = permissions_request.update(per_project_permissions.model_dump())

@pytest.fixture(scope="session", params=Config().get_browser_config()) # параметризируем фикстуру на будущее, чтобы можно было запускать в разных браузерах, браузеры в конфиге
def driver(request):
    browser, version = request.param
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", browser)  #  указываем браузер
    options.set_capability("browserVersion", version)  # указываем версию
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--window-size={Config().properties.browsers.browser_size}")

    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableLog": True
    })

    driver = webdriver.Remote(
        command_executor=Config().properties.servers.dev.selenoid_url,
        options=options
    )
    yield driver

    if driver:
        driver.quit()