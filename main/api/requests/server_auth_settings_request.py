from main.api.configs.config import Config
from main.api.requests.base_request import Request
from main.api.requests.endpoints import Endpoint
from main.api.specs.specifications import Specifications


class ServerAuthSettingRequest(Request):

    def __init__(self, specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self):
        response = self.session.get(f"{Config().properties.servers.dev.base_url}{self.endpoint}")
        return response

session = Specifications()
test = ServerAuthSettingRequest(session.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
responce = test.read()
print(responce)