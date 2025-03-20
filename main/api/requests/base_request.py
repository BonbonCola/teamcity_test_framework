from abc import ABC, abstractmethod


class Request():
    # Request - это класс, описывающий меняющиеся параметры запроса, такие как: спецификация, эндпоинт (relative URL, model)
    def __init__(self, specifications, endpoint):
        self.session = specifications
        self.endpoint = endpoint

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
