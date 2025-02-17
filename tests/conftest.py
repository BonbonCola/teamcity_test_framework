import sys
import os
import random

import pytest
from faker import Faker
from pydantic import BaseModel
from typing import List

from main.api.models.api_models import Project, BuildType, Steps, Step
from main.api.models.user_model import User, Roles, Role, Property, Properties

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def generate_test_user(role_id=None, scope_type=None):
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
    """Генерирует тестовый проект"""
    fake = Faker()
    return Project(
        id=fake.word(),
        name=fake.company(),
        locator="_Root"
    )

def generate_test_build_type(project: Project):
    """Генерирует тестовый BuildType, привязанный к переданному проекту"""
    fake = Faker()
    return BuildType(
        id=fake.word(),
        name=fake.word(),
        project=project,

    )
