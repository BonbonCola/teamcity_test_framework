from main.api.requests.base_request import BaseCRUDRequest, Request
from main.api.requests.unchecked_crud_request import UncheckedRequest
from main.exceptions import BadRequestException
from tests.helpers.test_data_storage import TestDataStorage


class CheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, specifications, endpoint):
        self.unchecked_request = UncheckedRequest(specifications, endpoint)
        super().__init__(specifications, endpoint)

    def create(self, model):
        response = self.unchecked_request.create(model)
        if response.status_code not in [200, 201]:
            raise BadRequestException(response)
        TestDataStorage().add_created_entity(self.endpoint, response.json())
        return response


    def read(self, id):
        response = self.unchecked_request.read(id)
        if response.status_code != 200:
            raise BadRequestException(response)
        return response

    def update(self, id, model):
        response = self.unchecked_request.update(id, model)
        if response.status_code != 200:
            raise BadRequestException(response)
        return response


    def delete(self, id):
        response = self.unchecked_request.delete(id)
        if response.status_code != 200:
            raise BadRequestException(response)
        return response