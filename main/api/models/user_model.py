from pydantic import BaseModel # аналог Java Lombok + валидация полей

class Property(BaseModel):
    name: str
    value: str

class Properties(BaseModel):
    property: list[Property]

class Role(BaseModel):
    roleId: str
    scope: str

class Roles(BaseModel):
    role: list[Role]

class User(BaseModel):
    username: str
    password: str
    email: str
    roles: Roles
    properties: Properties

# Возможные роли
#TODO: сделать  enum
role_id = [
    "PROJECT_VIEWER", "PROJECT_DEVELOPER", "PROJECT_ADMIN",
    "AGENT_MANAGER", "TOOLS_INTEGRATION", "GUEST_ROLE",
    "USER_ROLE", "SYSTEM_ADMIN"
]

# Возможные области (scopes)
scope = ["g", "p:{project_id}", "bt:{build_type_id}", "vcs:{vcs_root_id}"]