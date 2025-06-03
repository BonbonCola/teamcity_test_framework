import logging

# Настройка логирования
def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG, # минимальный уровень для root-логгера
        format="%(asctime)s – %(name)s – %(levelname)s – %(message)s",
        handlers=[
            logging.StreamHandler(),  # Вывод в консоль
        ]
    )