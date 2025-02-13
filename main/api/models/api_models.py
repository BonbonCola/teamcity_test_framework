from pydantic import BaseModel # аналог Java Lombok + валидация полей

class Project(BaseModel):
    id: str
    name: str
    locator: str = "_Root"

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
    steps: Steps