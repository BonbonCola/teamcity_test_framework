from tokenize import endpats

from main.api.configs.config import Config
from main.api.crud_requests.base_crud_request import BaseCRUDRequest, Request
from main.api.specs.specifications import Specifications


class UncheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, specifications: Specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self, id):
        response = self.session.get(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}")
        print(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def update(self, id, model):
        response = self.session.put(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}", json=model)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def delete(self, id):
        response = self.session.delete(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def create(self, model):
        response = self.session.post(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}", json=model)
        print(f"http://{Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response
