from pydantic import BaseModel # аналог Java Lombok + валидация полей
from typing import Optional

class ParentProject(BaseModel):
    locator: str

class SourceProject(BaseModel):
    locator: str

class Project(BaseModel):
    id: str
    name: str
    locator: Optional[str] = None
    parentProject: Optional[ParentProject] = None
    sourceProject: Optional[SourceProject] = None

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