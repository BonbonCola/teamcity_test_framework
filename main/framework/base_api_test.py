import pytest
from main.api.specs.specifications import Specifications
from main.api.configs.config import Config
from main.api.models.user_model import User


class BaseApiTest:
    def setup_method(self): #метод, который выполняется перед тестами
        """ Подключает API-сессию ко всем тестам """
        self.specifications = Specifications()
        self.base_url = self.specifications.get_config().properties.servers.dev.base_url
        self.user = User(username=self.specifications.get_config().properties.servers.dev.username, password=self.specifications.get_config().properties.servers.dev.password)
        self.session = self.specifications.get_auth_session(self.user)