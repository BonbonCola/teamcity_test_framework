from main.api.specs.specifications import Specifications
from main.api.models.user_model import User
from main.framework.base_test import BaseTest


class BaseApiTest(BaseTest):
    def setup_method(self): #метод, который выполняется перед тестами
        super().setup_method()
        """ Подключает API-сессию ко всем тестам """
        self.specifications = Specifications()
        self.base_url = self.specifications.config.servers.dev.base_url
