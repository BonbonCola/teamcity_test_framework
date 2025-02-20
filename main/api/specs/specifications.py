import requests
import logging
from main.api.configs.config import Config

class Specifications:

    def __init__(self):
        self.session = requests.Session()  # создаем сессию
        self.config = Config().properties # берем конфиг
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def authSpec(self, user):
        auth = user.username, user.password  # считываем пользователя и пароль из конфига
        self.session.cookies = requests.cookies.RequestsCookieJar()
        self.session.auth = auth  # и добавляем в текущую сессию
        return self.session

    def unAuthSpec(self):
        return self.session

    def superUserSpec(self):
        auth = "", self.config.servers.dev.superusertoken
        self.session.cookies = requests.cookies.RequestsCookieJar()
        self.session.auth = auth
        return self.session




