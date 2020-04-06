from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class FooterSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    footer_section = {"by": By.CSS_SELECTOR, "value": '#footer'}

    logo_footer = {"by": By.CSS_SELECTOR, "value": '#footer > div.botpart > div > div.botpart__logo > a > img'}

    privacy_link = {"by": By.CSS_SELECTOR,
                    "value": '#footer > div.botpart > div > div.botpart__items > div:nth-child(1) > a'}
    terms_link = {"by": By.CSS_SELECTOR,
                  "value": '#footer > div.botpart > div > div.botpart__items > div:nth-child(2) > a'}
    sitemap_link = {"by": By.CSS_SELECTOR,
                    "value": '#footer > div.botpart > div > div.botpart__items > div:nth-child(3) > a'}
    locations_link = {"by": By.CSS_SELECTOR,
                      "value": '#footer > div.botpart > div > div.botpart__items > div:nth-child(4) > a'}
    copyright_logo = {"by": By.CSS_SELECTOR, "value": '#footer > div.botpart > div > div.botpart__copyright > div'}

    slb_shares = {"by": By.CSS_SELECTOR,
                  "value": '#footer > div.botpart > div > div.botpart__ticker.botpart__ticker--available > span.company'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def get_footer_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#footer > div.toppart.row.small-collapse.large-uncollapse.accordion > div')
        return elems

    def footer_items_count(self):
        return len(self.get_footer_items())

    def get_social_links_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#footer > div.botpart > div > div.botpart__social > div > a')
        return elems

    def social_items_count(self):
        return len(self.get_social_links_items())

    def find_items(self, item):
        return self._find(item)

    def footer_section_is_displayed(self):
        return self._is_displayed(self.footer_section)

    def scroll_to_footer_section(self):
        return self._scroll_to_element(self.footer_section)

    def logo_footer_is_displayed(self):
        return self._is_displayed(self.logo_footer)

    def privacy_link_get_text(self):
        return self._get_text(self.privacy_link)

    def terms_link_get_text(self):
        return self._get_text(self.terms_link)

    def sitemap_link_get_text(self):
        return self._get_text(self.sitemap_link)

    def locations_link_get_text(self):
        return self._get_text(self.locations_link)

    def copyright_logo_get_text(self):
        return self._get_text(self.copyright_logo)

    def slb_shares_get_text(self):
        return self._get_text(self.slb_shares)
