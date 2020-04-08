import time

import pytest

from pages import wikipedia_login


class TestLoginCredentials():
    @pytest.fixture
    def login(self, driver):
        return wikipedia_login.WikipediaPage(driver)

    def test_login_credentials(self, driver, login):
        login.navigate_to_wikipedia()
        time.sleep(2)
        login.click_on_english_language_option()
        time.sleep(2)
        login.click_on_login_cta_button()
        time.sleep(2)

        login.fill_in_login_credentials("AndreiCJR", "Usource2020!")
        time.sleep(2)
        login.click_on_login()