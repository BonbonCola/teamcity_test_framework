from urllib.request import build_opener

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from main.ui.base_element import BaseElement


class ProjectElement(BaseElement):
    def __init__(self, element: WebElement):
        super().__init__(element)
        self.project_name = (By.CSS_SELECTOR, "span[class*='MiddleEllipsis']")

    def get_name(self):
        name = self.find(self.project_name)
        return name.text
