from http.client import responses

import requests
import pytest
import logging
from main.framework.base_api_test import BaseApiTest

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class TestDummy(BaseApiTest):
    def test_example(self):  # Имя метода должно начинаться с test_
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        logger.info(f"Отправляем GET-запрос с заголовками")
        response =  requests.get("http://admin:admin@localhost:8111/app/rest/projects", headers=headers)
        logger.info(f"Ответ API: статус {response.status_code}, тело {response.text}")
        assert response.status_code == 200

    def test_get_projects(self):
        """ Тест на получение списка проектов """
        response = self.session.get(f"http://{self.base_url}/app/rest/projects")
        print(f"Ответ API: {response.json()}")
        assert response.status_code == 200, f"Ошибка: {response.status_code}"