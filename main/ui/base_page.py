from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import logging
logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver  #передаем driver
        self.timeout = 30
        self.long_timout = 180

    def find(self, locator, timeout=30):
        """Обертка для поиска элемента"""
        logger.info(f"Начинаем поиск элемента {locator} с таймаутом {timeout} сек")
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f"Элемент {locator} найден на странице")
            return element
        except TimeoutException:
            logger.error(f"Не удалось найти элемент {locator} за {timeout} сек", exc_info=True)
            raise

    def find_all(self, locator, timeout=30):
        """Ожидает и возвращает список всех видимых элементов."""
        logger.info(f"Начинаем поиск элементов {locator} с таймаутом {timeout} сек")
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            logger.info(f"Элементы {locator} найдены на странице")
            return elements
        except TimeoutException:
            logger.error(f"Не удалось найти элементы {locator} за {timeout} сек", exc_info=True)
            raise

    def click(self, locator):
        """Обертка для клика по элементу"""
        logger.info(f"Пытаемся кликнуть на элемент {locator}")
        try:
            element = self.find(locator)
            element.click()
            logger.info(f"Кликнули на элемент {locator}")
        except (TimeoutException, NoSuchElementException):
            logger.error(f"Не удалось кликнуть элемент {locator}", exc_info=True)
            raise

    def type(self, locator, text):
        """Обертка для ввода текста"""
        logger.info(f"Пытаемся ввести текст в инпут {locator}")
        try:
            element = self.find(locator)
            element.clear()
            element.send_keys(text)
            logger.info(f"Текст в инпут {locator} введен")
        except (TimeoutException, NoSuchElementException):
            logger.error(f"Не удалось добавить текст в инпут {locator}", exc_info=True)
            raise