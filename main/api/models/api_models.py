from pydantic import BaseModel # аналог Java Lombok + валидация полей
from typing import Optional

class ParentProjectLocator(BaseModel):
    locator: str

class Project(BaseModel):
    id: str
    name: str
    locator: str = "_Root"
    parentProjectLocator: Optional[ParentProjectLocator] = None

class Step(BaseModel):
    id: str
    name: str
    type: str = "simpleRunner"

class Steps(BaseModel):
    count: int
    steps: list[Step]

class BuildType(BaseModel):
    id: str
    name: str
    project: Project
    steps:  Optional[Steps] = None