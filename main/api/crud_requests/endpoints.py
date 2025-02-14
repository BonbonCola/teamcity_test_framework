from enum import Enum
from typing import Type
from pydantic import BaseModel
from main.api.models.api_models import BuildType, Project

class Endpoint(Enum):
    BUILD_TYPES = ("/app/rest/buildTypes", BuildType)
    PROJECTS = ("/app/rest/projects", Project)

    def __init__(self, url: str, model_class: Type[BaseModel]):
        self.url = url
        self.model_class = model_class
