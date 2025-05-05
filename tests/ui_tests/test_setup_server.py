import pytest

from main.ui.first_start_page import FirstStartPage
from main.ui.login_page import LoginPage


@pytest.mark.setup
class TestSetupServer():

    def test_setup_teamcity_server(self, driver):
        setup_page = FirstStartPage.open(driver)
        setup_page.setup_first_start()
        login_page = LoginPage.open(driver)
        login_page.create_admin_user()