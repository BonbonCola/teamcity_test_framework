from main.api.crud_requests.base_crud_request import BaseCRUDRequest, Request


class UncheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, Specifications, Endpoint):
        super().__init__(Specifications, Endpoint)

    def read(self, id):
        response = self.session.get_auth_session.get(f"http://{self.endpoint.BUILD_TYPES.url}/id:{id}")
        return response

    def update(self, id, model):
        response = self.session.get_auth_session.put(f"http://{self.endpoint.BUILD_TYPES.url}/id:{id}", model)
        return response

    def delete(self, id):
        response = self.session.get_auth_session.delete(f"http://{self.endpoint.BUILD_TYPES.url}/id:{id}")
        return response

    def create(self, model):
        response = self.session.get_auth_session.post(f"http://{self.endpoint.BUILD_TYPES.url}", model)
        return response
