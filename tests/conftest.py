import sys
import os
from copy import copy

import pytest
from faker import Faker
from collections import defaultdict

from selenium import webdriver
from main.api.configs.config import Config

from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.api.models.api_models import ParentProject, Project, BuildType, SourceProject
from main.api.models.user_model import User, Roles, Role, Property, Properties, scope

from main.api.models.server_auth_settings import ServerAuthSettings
from main.api.requests.endpoints import Endpoint
from main.api.requests.server_auth_settings_request import ServerAuthSettingRequest
from main.api.specs.specifications import Specifications

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def generate_test_user(role_id="PROJECT_ADMIN", scope_type="g"):
    """Генерирует тестового пользователя с ролью и областью"""
    fake = Faker()
    return User(
        username=fake.user_name(),
        password=fake.password(),
        email=fake.email(),
        roles=Roles(role=[
            Role(roleId=role_id, scope=scope_type)
        ]),
        properties=Properties(property=[
            Property(name="prop1", value=fake.word())
        ])
    )

def generate_test_project():
    """Генерирует тестовый root проект"""
    fake = Faker()
    return Project(
        id=fake.word(),
        name=fake.word(),
        locator="_Root"
    )

def generate_test_child_project(parent_project: Project):
    """Генерирует тестовый child проект"""
    fake = Faker()
    parent_project_id = ParentProject(locator = parent_project.id)
    return Project(
        id=fake.word(),
        name=fake.word(),
        parentProject=parent_project_id
    )

def generate_test_copy_project(source_project, parent_project=None):
    """Добавляет проект копирования."""
    fake = Faker()
    locator = "_Root"

    source_project_id = SourceProject(locator = source_project.id)

    if not source_project:
        raise ValueError("sourceProject должен быть передан")

    return Project(
        id=fake.word(),
        name=fake.word(),
        locator=locator if parent_project is None else parent_project.id,
        sourceProject=source_project_id
    )

def generate_test_build_type(project: Project):
    """Генерирует тестовый BuildType, привязанный к переданному проекту"""
    fake = Faker()
    del(project.locator)
    return BuildType(
        id=fake.word(),
        name=fake.word(),
        project=project,

    )

class TestData():
    def __init__(self):
        self.user = generate_test_user()
        self.project = generate_test_project()
        self.project.locator
        self.buildtype = generate_test_build_type(self.project)
        self.child_project = generate_test_child_project(self.project)

class TestDataStorage:
    """Синглтон-класс для хранения тестовых данных"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestDataStorage, cls).__new__(cls)
            cls._instance.created_entities = defaultdict(set)
        return cls._instance

    def add_created_entity(self, endpoint: Endpoint, model):
        """Добавляет созданную сущность в хранилище"""
        entity_id = self._get_entity_id_or_locator(model)
        if entity_id:
            self.created_entities[endpoint].add(entity_id)

    def _get_entity_id_or_locator(self, model):
        """Пытается получить `id` или `locator` у объекта"""
        return model["id"] or model["locator"]

    def delete_created_entities(self):
        """Удаляет все созданные сущности после теста"""
        for endpoint, entity_ids in self.created_entities.items():
            for entity_id in entity_ids:
                UncheckedRequest(Specifications().superUserSpec(), endpoint).delete(entity_id)
        self.created_entities.clear()

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