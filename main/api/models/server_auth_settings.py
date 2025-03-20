from pydantic import BaseModel


class Module(BaseModel):
    name: str = "Default"

class ServerAuthSettings(BaseModel):
    perProjectPermissions: bool
    module: list[Module]
