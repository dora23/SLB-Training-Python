from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class Header(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    header_section = {"by": By.CSS_SELECTOR, "value": 'body > header > div:nth-child(1)'}
    slb_logo = {"by": By.CSS_SELECTOR, "value": 'div:nth-child(1) > div > div.logo'}
    who_we_are = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__mainnav > ul > li:nth-child(1) > a'}
    newsroom = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__mainnav > ul > li:nth-child(2) > a'}
    careers = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__mainnav > ul > li:nth-child(3) > a'}
    investor = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__mainnav > ul > li:nth-child(4) > a'}
    global_stewardship = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__mainnav > ul > li:nth-child(5) > a'}
    search_field = {"by": By.CLASS_NAME, "value": 'magic-box-input'}
    search_field_active = {"by": By.CSS_SELECTOR, "value": 'div.magic-box-input > input'}
    search_button = {"by": By.CSS_SELECTOR, "value": '#searchbox > a > span.coveo-search-button'}
    sign_in_button = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__actions > a.mainbar__actions__btn.btn--sign-in'}
    contact_button = {"by": By.CSS_SELECTOR, "value": 'div.mainbar__actions > a.mainbar__actions__btn.btn--order'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def header_section_is_displayed(self):
        return self._is_displayed(self.header_section)

    def slb_logo_is_displayed(self):
        return self._is_displayed(self.slb_logo)

    # -------------------Who We Are-----------------------------------------
    def who_we_are_is_displayed(self):
        return self._is_displayed(self.who_we_are)

    def click_on_who_we_are(self):
        self._click(self.who_we_are)

    # -------------------Newsroom-----------------------------------------

    def newsroom_is_displayed(self):
        return self._is_displayed(self.newsroom)

    def click_on_newsroom(self):
        self._click(self.newsroom)

    # -------------------Careers-----------------------------------------

    def careers_is_displayed(self):
        return self._is_displayed(self.careers)

    def click_on_careers(self):
        self._click(self.careers)

    # -------------------Investors-----------------------------------------

    def investor_is_displayed(self):
        return self._is_displayed(self.investor)

    def click_on_investor(self):
        self._click(self.investor)

    # -------------------Global Stewardship-----------------------------------------
    def global_stewardship_is_displayed(self):
        return self._is_displayed(self.global_stewardship)

    def click_on_global_stewardship(self):
        self._click(self.global_stewardship)

    # -------------------Search-----------------------------------------
    def search_field_is_displayed(self):
        return self._is_displayed(self.search_field)

    def click_in_search_field(self):
        self._click(self.search_field)

    def search_function(self, text):
        self._type(self.search_field_active, text)

    def get_current_url_link(self):
        return self._get_current_url()

    def click_on_search_button(self):
        self._click(self.search_button)

    def sign_in_button_is_displayed(self):
        return self._is_displayed(self.sign_in_button)

    def contact_button_is_displayed(self):
        return self._is_displayed(self.contact_button)
