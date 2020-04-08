from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import wikiurl


class WikipediaPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    english_language_option = {"by": By.CSS_SELECTOR,
                    "value": '#js-link-box-en > strong'}

    login_cta_button = {"by": By.CSS_SELECTOR,
                               "value": '#pt-login > a'}

    username_area = {"by": By.CSS_SELECTOR,
                            "value": 'input[id="wpName1"]'}

    password_area = {"by": By.CSS_SELECTOR,
                     "value": 'input[id="wpPassword1"]'}

    login = {"by": By.CSS_SELECTOR,
                               "value": '#wpLoginAttempt'}

    def navigate_to_wikipedia(self):
        self._visit(wikiurl)

    def click_on_english_language_option(self):
        self._click(self.english_language_option)

    def click_on_login_cta_button(self):
        self._click(self.login_cta_button)

    def click_on_login(self):
        self._click(self.login)


    def fill_in_login_credentials(self, username, password):
        self._click(self.username_area)
        self._type(self.username_area, username)
        self._click(self.password_area)
        self._type(self.password_area, password)