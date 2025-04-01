from main.api.configs.config import Config
from main.api.requests.base_request import Request


class ServerAuthSettingRequest(Request):

    def __init__(self, specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self):
        response = self.session.get(f"{Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"GET {Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"Status code:{response.status_code}")
        return response

    def update(self, data):
        response = self.session.put(f"{Config().properties.servers.dev.base_url}{self.endpoint}", json=data)
        print(f"PUT {Config().properties.servers.dev.base_url}{self.endpoint}")
        print(f"Status code:{response.status_code}")
        return response
