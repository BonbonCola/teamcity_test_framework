from main.api.configs.config import Config
from main.api.requests.base_request import BaseCRUDRequest, Request
from main.api.specs.specifications import Specifications

import logging
logger = logging.getLogger(__name__)

class UncheckedRequest(BaseCRUDRequest, Request):

    def __init__(self, specifications: Specifications, endpoint):
        super().__init__(specifications, endpoint)

    def read(self, locator):
        response = self.session.get(f"{Config().properties.servers.dev.base_url}{self.endpoint}/{locator}")
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response

    def update(self, id, model):
        response = self.session.put(f"{Config().properties.servers.dev.internal_base_url}{self.endpoint}/id:{id}", json=model)
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response

    def delete(self, id):
        response = self.session.delete(f"{Config().properties.servers.dev.base_url}{self.endpoint}/id:{id}")
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response

    def create(self, model):
        response = self.session.post(f"{Config().properties.servers.dev.base_url}{self.endpoint}", json=model)
        logger.info(f"{response.request.method} URL: {response.request.url}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        return response
