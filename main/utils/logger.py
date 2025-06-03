import logging

# Настройка логирования
def configure_logging():
    logging.basicConfig(
        level=logging.INFO, # минимальный уровень для root-логгера
        format="%(asctime)s – %(name)s – %(levelname)s – %(message)s", #Формат: время – имя логгера – уровень – сообщение
        handlers=[
            logging.StreamHandler(),  # Вывод в консоль
        ]
    )
    #«Заглушаем» шум от ненужных модулей:
    #logging.getLogger("selenium").setLevel(logging.INFO)  # пример: selenium меньше подробностей
    logging.getLogger("faker.factory").setLevel(logging.WARNING)  # отключаем шум от faker.factory
    logging.getLogger("faker").setLevel(logging.WARNING)