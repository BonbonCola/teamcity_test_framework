# он должен быть синглтоном
# конфигурация, делает запросы в тестах конфигурируемыми

from dynaconf import Dynaconf #для работы с конфигами
from pathlib import Path

class Config:
    _instance = None # Храним единственный экземпляр

    def __new__(cls, *args, **kwargs):  # cls - это сам класс Singleton
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance  # возвращаем один и тот же объект

    def __init__(self):
        CONFIG_PATH = Path(__file__).resolve().parent
        self.properties = Dynaconf(settings_files=[CONFIG_PATH/"env_config.toml"])  # считываем конфиг в properties

    def get_config(self):
        return (self._instance)


