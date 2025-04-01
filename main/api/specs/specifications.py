import requests
from main.api.configs.config import Config

class Specifications:

    def __init__(self):
        self.config = Config().properties # берем конфиг

    def authSpec(self, user):
        session = requests.Session()  # создаем сессию
        session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        auth = user.username, user.password  # считываем пользователя и пароль 
        session.auth = auth  # и добавляем в текущую сессию
        return session

    def unAuthSpec(self):
        session = requests.Session()
        session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        return session

    def superUserSpec(self):
        session = requests.Session()
        session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        auth = "", self.config.servers.dev.superusertoken
        session.cookies = requests.cookies.RequestsCookieJar()
        session.auth = auth
        return session




