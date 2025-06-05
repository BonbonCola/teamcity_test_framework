from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import logging
logger = logging.getLogger(__name__)

class BaseElement:

    def __init__(self, element: WebElement):
        self.element = element  #передаем driver

    def find(self, locator) -> WebElement:
        logger.info(f"Начинаем поиск элемента {locator}")
        try:
            element = WebDriverWait(self.element, 30).until(EC.visibility_of_element_located(locator))
            logger.info(f"Элемент {locator} найден на странице")
            return element
        except TimeoutException:
            logger.error(f"Не удалось найти элемент {locator}", exc_info=True)
            raise

    def find_all(self, locator):
        logger.info(f"Начинаем поиск элементов {locator}")
        try:
            elements = WebDriverWait(self.element).until(EC.presence_of_all_elements_located(locator))
            logger.info(f"Элементы {locator} найдены на странице")
            return elements
        except TimeoutException:
            logger.error(f"Не удалось найти элементы {locator}", exc_info=True)
            raise

    def click(self, locator):
        logger.info(f"Пытаемся кликнуть на элемент {locator}")
        try:
            element = self.find(locator)
            element.click()
            logger.info(f"Кликнули на элемент {locator}")
        except (TimeoutException, NoSuchElementException):
            logger.error(f"Не удалось кликнуть элемент {locator}", exc_info=True)
            raise