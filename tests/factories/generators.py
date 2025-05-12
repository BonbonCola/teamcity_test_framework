from faker import Faker

from main.api.models.api_models import ParentProject, Project, BuildType, SourceProject
from main.api.models.user_model import User, Roles, Role, Property, Properties, scope

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