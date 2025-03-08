from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from main.ui.base_element import BaseElement


class ProjectElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)
        self.name = (By.CSS_SELECTOR, "span[class*='MiddleEllipsis']")
        self.link = (By.TAG_NAME, "a")
        self.button = (By.TAG_NAME, "button")

    def get_name(self):
        name = self.find(self.name)
        return name.text
