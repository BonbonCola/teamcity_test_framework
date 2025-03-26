from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, element: WebElement):
        self.element = element  #передаем driver

    def find(self, locator) -> WebElement:
        return WebDriverWait(self.element, 30).until(  # ждем 30 сек, пока элемент не появится
            EC.visibility_of_element_located(locator)  # элемент виден, находим его и возвращаем
        )

    def find_all(self, locator):
        return WebDriverWait(self.element, 30).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        self.find(locator).click()