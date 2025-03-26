from main.api.requests.base_request import BaseCRUDRequest, Request
from main.api.requests.unchecked_crud_request import UncheckedRequest

from tests.conftest import TestDataStorage


class CheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, specifications, endpoint):
        self.unchecked_request = UncheckedRequest(specifications, endpoint)
        super().__init__(specifications, endpoint)

    def create(self, model):
        response = self.unchecked_request.create(model)
        #TODO: переделать на использование исключений
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        TestDataStorage().add_created_entity(self.endpoint, response.json())
        return response


    def read(self, id):
        response = self.unchecked_request.read(id)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return response

    def update(self, id, model):
        response = self.unchecked_request.update(id, model)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return response


    def delete(self, id):
        response = self.unchecked_request.delete(id)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return response