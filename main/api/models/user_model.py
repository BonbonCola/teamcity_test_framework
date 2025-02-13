from pydantic import BaseModel # аналог Java Lombok + валидация полей

class User(BaseModel):
    username: str
    password: str
