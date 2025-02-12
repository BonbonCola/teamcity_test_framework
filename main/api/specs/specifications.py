import requests
import logging
from main.api.configs.config import Config

class Specifications:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._instance.session = requests.Session()  # создаем сессию
        self._instance.config = Config()  # берем конфиг
        self._instance.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self._instance.session

    def get_auth_session(self, user):
        """ Возвращает сессию requests.Session() с предустановленными заголовками и авторизацией """
        auth = user.username, user.password  # считываем пользователя и пароль из конфига
        self._instance.session.auth = auth  # и добавляем в текущую сессию
        return self._instance.session

    def get_unauth_session(self):
        """ Возвращает сессию requests.Session() без авторизации """
        return self._instance.session

    def get_config(self):
        """ Возвращает конфиг """
        return self._instance.config


