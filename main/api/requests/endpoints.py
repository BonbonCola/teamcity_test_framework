from enum import Enum
from typing import Type
from pydantic import BaseModel
from main.api.models.api_models import BuildType, Project
from main.api.models.server_auth_settings import ServerAuthSettings
from main.api.models.user_model import User


class Endpoint(Enum):
    BUILD_TYPES = ("/app/rest/buildTypes", BuildType)
    PROJECTS = ("/app/rest/projects", Project)
    USERS = ("/app/rest/users", User)
    AUTH_SETTINGS = ("/app/rest/server/authSettings", ServerAuthSettings)

    def __init__(self, url: str, model_class: Type[BaseModel]):
        self.url = url
        self.model_class = model_class
