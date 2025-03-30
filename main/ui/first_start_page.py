from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main.api.configs.config import Config
from selenium.webdriver.common.by import By

from main.ui.base_page import BasePage

from selenium.webdriver.common.keys import Keys


class FirstStartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.button_proceed = (By.ID, "proceedButton")
        self.db_type = (By.ID, "dbType")
        self.agreement = (By.CLASS_NAME, "licenseAgreement")
        self.checkbox_agree = (By.CSS_SELECTOR, "label[for='accept']")
        self.button_continue = (By.CSS_SELECTOR, "input.btn.btn_primary.submitButton")
        self.scrollable_div = (By.TAG_NAME, "body")

    @classmethod
    def open(cls, driver):
        driver.get(f"{Config().properties.servers.dev.internal_base_url}/mnt")
        return cls(driver)

    def setup_first_start(self):
        print(f"ПЫТАЕМСЯ НАЙТИ КНОПКУ")
        #self.find(self.button_proceed, timeout=380)
        print("Current URL:", self.driver.current_url)
        #self.driver.execute_script("document.getElementById('proceedButton').removeAttribute('disabled')")
        #self.click(self.button_proceed)
        self.driver.refresh()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "submitButton"))  # или любой другой JS-индикатор
        )
        print("Page source:")
        print(self.driver.page_source[:10000])
        self.driver.save_screenshot("teamcity_fail.png")
        self.driver.execute_script("BS.Maintenance.FirstStart.submit(false);")
        self.find(self.db_type, self.long_timout)
        self.click(self.button_proceed)
        self.find(self.agreement)

        agreement = self.find(self.scrollable_div)
        agreement.send_keys(Keys.END)

        self.find(self.checkbox_agree)
        self.click(self.checkbox_agree)
        self.click(self.button_continue)


