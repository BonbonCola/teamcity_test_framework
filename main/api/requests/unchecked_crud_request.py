from main.api.configs.config import Config
from main.api.requests.base_request import BaseCRUDRequest, Request
from main.api.specs.specifications import Specifications


class UncheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, specifications: Specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self, locator):
        response = self.session.get(f"{Config().properties.servers.dev.base_url}{self.endpoint}/{locator}")
        print(f"GET http://{Config().properties.servers.dev.base_url}{self.endpoint}/{locator}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def update(self, id, model):
        response = self.session.put(f"{Config().properties.servers.dev.internal_base_url}{self.endpoint}/id:{id}", json=model)
        print(f"PUT {Config().properties.servers.dev.internal_base_url}{self.endpoint}/id:{id}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def delete(self, id):
        response = self.session.delete(f"{Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}")
        print(f"DELETE {Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response

    def create(self, model):
        response = self.session.post(f"{Config().properties.servers.dev.base_url}{self.endpoint}", json=model)
        print(f"POST http://{Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return response
