import pytest

from main.framework.base_ui_test import BaseUiTest
from main.ui.first_start_page import FirstStartPage

@pytest.mark.setup
class TestSetupServer(BaseUiTest):

    def test_setup_teamcity_server(self):
        setup_page = FirstStartPage.open(self.driver)
        setup_page.setup_first_start()