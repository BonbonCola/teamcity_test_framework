from abc import ABC, abstractmethod
from main.api.crud_requests import endpoints

class BaseCRUDRequest(ABC):

    @abstractmethod
    def create(self, model):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, id, model):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class Request():
    # Request - это класс, описывающий меняющиеся параметры запроса, такие как: спецификация, эндпоинт (relative URL, model)
    def __init__(self, Specifications, Endpoint):
        self.session = Specifications,
        self.endpoint = Endpoint