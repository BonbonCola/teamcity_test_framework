from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:

    def __init__(self, element: WebElement):
        self.element = element  #передаем driver

    def find(self, locator) -> WebElement:
        return self.element.find_element(locator)

    def find_all(self, locator):
        return self.element.find_elements(locator)