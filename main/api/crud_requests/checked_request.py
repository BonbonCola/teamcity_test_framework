from main.api.crud_requests.base_crud_request import BaseCRUDRequest, Request
from main.api.crud_requests.unchecked_request import UncheckedRequest
from typing import Type
from pydantic import BaseModel


class CheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, Specifications, Endpoint):
        self.unchecked_request = UncheckedRequest()
        super().__init__(Specifications, Endpoint)

    def create(self, model):
        response = self.unchecked_request.create(model)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        model_class: Type[BaseModel] = self.endpoint.model_class
        return model_class.model_validate(response.json())


    def read(self, id):
        response = self.unchecked_request.read(id)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        # Десериализуем JSON-ответ в соответствующий Pydantic-класс
        model_class: Type[BaseModel] = self.endpoint.model_class
        return model_class.model_validate(response.json())

    def update(self, id, model):
        response = self.unchecked_request.update(id, model)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        model_class: Type[BaseModel] = self.endpoint.model_class
        return model_class.model_validate(response.json())


    def delete(self, id):
        response = self.unchecked_request.delete(id)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return response.json()