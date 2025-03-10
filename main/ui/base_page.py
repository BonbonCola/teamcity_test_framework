from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver  #передаем driver

    def find(self, locator):
        """Обертка для поиска элемента"""
        return WebDriverWait(self.driver, 30).until( #ждем 30 сек, пока элемент не появится
            EC.visibility_of_element_located(locator) #элемент виден, находим его и возвращаем
        )

    def find_all(self, locator):
        """Ожидает и возвращает список всех видимых элементов."""
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        """Обертка для клика по элементу"""
        self.find(locator).click()

    def type(self, locator, text):
        """Обертка для ввода текста"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)