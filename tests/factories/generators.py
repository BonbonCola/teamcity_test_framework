from faker import Faker

from main.api.models.api_models import ParentProject, Project, BuildType, SourceProject
from main.api.models.user_model import User, Roles, Role, Property, Properties

class GenerateTest:

    @staticmethod
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

    @staticmethod
    def generate_test_project_full(parent_project=None, source_project=None):
        fake = Faker()
        locator = "_Root"

        project = Project(
            id=fake.word(),
            name=fake.word()
        )

        if parent_project is None:
            project.locator = locator
        else:
            parent_project_id = ParentProject(locator=parent_project.id)
            project.parentProject = parent_project_id
        if source_project is not None:
            source_project_id = SourceProject(locator=source_project.id)
            project.locator = locator if parent_project is None else parent_project.id,
            project.sourceProject = source_project_id
        return project

    @staticmethod
    def generate_test_build_type(project: Project):
        """Генерирует тестовый BuildType, привязанный к переданному проекту"""
        fake = Faker()
        del(project.locator)
        return BuildType(
            id=fake.word(),
            name=fake.word(),
            project=project,

        )