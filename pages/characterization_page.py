from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class CharacterizatonPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    in_menu_nav_bar = {"by": By.CSS_SELECTOR, "value": 'header > div.wrapper.show-for-large'}

    characterization_main_nav = {"by": By.CSS_SELECTOR, "value": '#mainnav__511e3bf8-27cb-4a88-8220-9f3df25c08c9 > a'}

    all_characterization_sub_nav = {"by": By.CSS_SELECTOR,
                                    "value": '#mega__511e3bf8-27cb-4a88-8220-9f3df25c08c9 > div.row > div.megamenu__all-link > div > a'}

    hero_section = {"by": By.CSS_SELECTOR, "value": 'section.hero-section > div.gradient'}

    hero_text_h1 = {"by": By.CSS_SELECTOR, "value": 'section.hero-section > div.hero-title > div.hero__title > h1'}

    hero_text_h2 = {"by": By.CSS_SELECTOR, "value": 'section.hero-section > div.hero-title > div.hero__tagline > h2'}

    sticky_banner = {"by": By.CSS_SELECTOR, "value": '#ctabanner'}

    contact_us = {"by": By.CSS_SELECTOR, "value": '#ctabanner > div > div > div:nth-child(1) > a > span'}

    related_documents = {"by": By.CSS_SELECTOR, "value": '#ctabanner > div > div > div:nth-child(2) > a > span'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def sticky_banner_is_displayed(self):
        return self._is_displayed(self.sticky_banner)

    def click_on_characterization_main_nav(self):
        self._click(self.characterization_main_nav)

    def click_on_all_characterization_sub_nav(self):
        self._click(self.all_characterization_sub_nav)

    def contact_us_is_displayed(self):
        return self._is_displayed(self.contact_us)

    def related_documents_is_displayed(self):
        return self._is_displayed(self.related_documents)

    def in_menu_nav_bar_is_displayed(self):
        return self._is_displayed(self.in_menu_nav_bar)

    def hero_section_is_displayed(self):
        return self._is_displayed(self.hero_section)

    def get_current_link(self):
        return self._get_current_url()

    def hero_text_h1_get_text(self):
        return self._get_text(self.hero_text_h1)

    def hero_text_h2_get_text(self):
        return self._get_text(self.hero_text_h2)