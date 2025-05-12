from collections import defaultdict

from main.api.requests.endpoints import Endpoint
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.api.specs.specifications import Specifications

class TestDataStorage:
    """Синглтон-класс для хранения тестовых данных"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestDataStorage, cls).__new__(cls)
            cls._instance.created_entities = defaultdict(set)
        return cls._instance

    def add_created_entity(self, endpoint: Endpoint, model):
        """Добавляет созданную сущность в хранилище"""
        entity_id = self._get_entity_id_or_locator(model)
        if entity_id:
            self.created_entities[endpoint].add(entity_id)

    def _get_entity_id_or_locator(self, model):
        """Пытается получить `id` или `locator` у объекта"""
        return model["id"] or model["locator"]

    def delete_created_entities(self):
        """Удаляет все созданные сущности после теста"""
        for endpoint, entity_ids in self.created_entities.items():
            for entity_id in entity_ids:
                UncheckedRequest(Specifications().superUserSpec(), endpoint).delete(entity_id)
        self.created_entities.clear()