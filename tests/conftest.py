import sys
import os
import random

import pytest
from faker import Faker
from pydantic import BaseModel
from typing import List
from collections import defaultdict

from main.api.crud_requests.endpoints import Endpoint
from main.api.crud_requests.unchecked_request import UncheckedRequest
from main.api.models.api_models import ParentProjectLocator, Project, BuildType
from main.api.models.user_model import User, Roles, Role, Property, Properties
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
        name=fake.company(),
        locator="_Root"
    )

def generate_test_child_project(parent_project: Project):
    """Генерирует тестовый child проект"""
    fake = Faker()
    parentProjectLocator = ParentProjectLocator(locator = parent_project.id)
    return Project(
        id=fake.word(),
        name=fake.company(),
        parentProjectLocator=parentProjectLocator
    )

def generate_test_build_type(project: Project):
    """Генерирует тестовый BuildType, привязанный к переданному проекту"""
    fake = Faker()
    return BuildType(
        id=fake.word(),
        name=fake.word(),
        project=project,

    )
#TODO: переделать на использование фикстур
class TestData():
    def __init__(self):
        self.user = generate_test_user()
        self.project = generate_test_project()
        self.project.locator = None
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
