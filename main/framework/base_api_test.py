from copy import copy

from main.api.models.server_auth_settings import ServerAuthSettings
from main.api.requests.endpoints import Endpoint
from main.api.requests.server_auth_settings_request import ServerAuthSettingRequest
from main.api.specs.specifications import Specifications
from main.api.models.user_model import User
from main.framework.base_test import BaseTest


class BaseApiTest(BaseTest):

    def setup_method(self): #метод, который выполняется перед тестами
        super().setup_method()
        """ Подключает API-сессию ко всем тестам """
        self.specifications = Specifications()
        self.base_url = self.specifications.config.servers.dev.base_url
        #Получаем текущие настройки per_project_permissions
        permissions_request = ServerAuthSettingRequest(self.specifications.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
        permissions_response = permissions_request.read()
        permissions_response_to_json = permissions_response.json()
        self.per_project_permissions = ServerAuthSettings(**permissions_response_to_json)
        #Обновляем значение per_project_permissions на true
        new_per_project_permissions = copy(self.per_project_permissions)
        new_per_project_permissions.perProjectPermissions = True
        update_permissions_request = ServerAuthSettingRequest(self.specifications.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
        update_permissions_request.update(new_per_project_permissions.model_dump())

    def teardown_method(self):
        super().teardown_method()
        #Возвращаем настройке perProjectPermissions исходное значение
        permissions_request = ServerAuthSettingRequest(self.specifications.superUserSpec(), Endpoint.AUTH_SETTINGS.url)
        permissions_response = permissions_request.update(self.per_project_permissions.model_dump())