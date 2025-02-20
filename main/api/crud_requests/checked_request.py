from main.api.crud_requests.base_crud_request import BaseCRUDRequest, Request
from main.api.crud_requests.unchecked_request import UncheckedRequest
from typing import Type
from pydantic import BaseModel

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