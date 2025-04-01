from pydantic import BaseModel
from typing import List, Optional


class Property(BaseModel):
    name: str
    value: str


class Properties(BaseModel):
    property: List[Property]


class Module(BaseModel):
    name: str
    properties: Optional[Properties] = None


class ModulesWrapper(BaseModel):
    module: List[Module]


class ServerAuthSettings(BaseModel):
    allowGuest: bool
    guestUsername: str
    collapseLoginForm: bool
    perProjectPermissions: bool
    emailVerification: bool
    modules: ModulesWrapper
