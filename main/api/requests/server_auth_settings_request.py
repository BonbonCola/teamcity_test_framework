from main.api.configs.config import Config
from main.api.requests.base_request import Request

import logging
logger = logging.getLogger(__name__)

class ServerAuthSettingRequest(Request):

    def __init__(self, specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self):
        response = self.session.get(f"{Config().properties.servers.dev.base_url}{self.endpoint}")
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response

    def update(self, data):
        response = self.session.put(f"{Config().properties.servers.dev.base_url}{self.endpoint}", json=data)
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response
