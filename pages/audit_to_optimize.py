from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl, audit_slb_url


class AuditPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    prod_cta_option = {"by": By.CSS_SELECTOR,
                    "value": '#mainnav__027c1327-8430-4224-aedb-b9b131f0a322 > a'}

    audit_cta_option = {"by": By.CSS_SELECTOR,
                       "value": '#mega__027c1327-8430-4224-aedb-b9b131f0a322 > div.row > div.megamenu__main > div:nth-child(1) > ul > li:nth-child(1) > a'}

    hero_section = {"by": By.CSS_SELECTOR,
                    "value": 'body > section.hero-section'}

    breadcrumbs = {"by": By.CSS_SELECTOR,
                       "value": 'div.breadcrumb__wrapper.absolute'}

    cta_banner = {"by": By.CSS_SELECTOR,
                       "value": '#ctabanner'}

    contact_us_cta = {"by": By.CSS_SELECTOR,
                      "value": '#ctabanner > div > div > div:nth-child(1) > a >'}

    related_documents_cta = {"by": By.CSS_SELECTOR,
                             "value": '#ctabanner > div > div > div:nth-child(2) > a'}

    two_col_component = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(5) > div'}

    two_col_component_text = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(5) > div > div:nth-child(1)'}

    two_col_component_image = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(5)'}

    hero_promo = {"by": By.CSS_SELECTOR,
                  "value": 'body > section.hero-promo'}

    hero_promo_cta_button = {"by": By.CSS_SELECTOR,
                  "value": 'body > section.hero-promo > div > div.small-12.medium-7.large-7.columns.no-padd > div > a'}

    second_two_col_component = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(7)'}

    second_two_col_component_text = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(7) > div > div:nth-child(2) > div'}

    second_two_col_component_image = {"by": By.CSS_SELECTOR,
                  "value": 'body > div:nth-child(7) > div > div:nth-child(1) > div'}

    h1 = {"by": By.CSS_SELECTOR,
                  "value": 'body > section.hero-section > div.hero-title > div.hero__title > h1'}

    h2 = {"by": By.CSS_SELECTOR,
                  "value": 'body > section.hero-section > div.hero-title > div.hero__tagline > h2'}

    related_information_banner = {"by": By.CSS_SELECTOR,
          "value": 'body > section:nth-child(9)'}

    related_information_title = {"by": By.CSS_SELECTOR,
                                  "value": 'body > section:nth-child(9) > div > div > div > a > div > div.content > h3'}

    related_information_description = {"by": By.CSS_SELECTOR,
                                  "value": 'body > section:nth-child(9) > div > div > div > a > div > div.content > p'}

    view_all_cta_button = {"by": By.CSS_SELECTOR,
                                  "value": 'body > section:nth-child(9) > div > a'}

    selected_option = {"by": By.CSS_SELECTOR,
          "value": 'div.selected-options > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def navigate_to_slb_audit(self):
        self._visit(audit_slb_url)

    def scroll_to_related_information_banner(self):
        return self._scroll_to_element(self.related_information_banner)

    def hero_title_get_text(self):
        return self._get_text(self.h1)

    def hero_subtitle_get_text(self):
        return self._get_text(self.h2)

    def selected_option_get_text(self):
        return self._get_text(self.selected_option)

    def related_information_title_get_text(self):
        return self._get_text(self.related_information_title)

    def related_information_description_get_text(self):
        return self._get_text(self.related_information_description)

    def click_on_prod_cta_option(self):
        self._click(self.prod_cta_option)

    def click_on_audit_cta_option(self):
        self._click(self.audit_cta_option)

    def click_on_view_all_cta_button(self):
        self._click(self.view_all_cta_button)

    def breadcrumbs_is_displayed(self):
        return self._is_displayed(self.breadcrumbs)

    def hero_section_is_displayed(self):
        return self._is_displayed(self.hero_section)

    def contact_us_cta_is_displayed(self):
        return self._is_displayed(self.contact_us_cta)

    def related_documents_cta_is_displayed(self):
        return self._is_displayed(self.related_documents_cta)

    def cta_banner_is_displayed(self):
        return self._is_displayed(self.cta_banner)

    def two_col_component_is_displayed(self):
        return self._is_displayed(self.two_col_component)

    def two_col_component_text_is_displayed(self):
        return self._is_displayed(self.two_col_component_text)

    def two_col_component_image_is_displayed(self):
        return self._is_displayed(self.two_col_component_image)

    def hero_promo_is_displayed(self):
        return self._is_displayed(self.hero_promo)

    def hero_promo_cta_button_is_displayed(self):
        return self._is_displayed(self.hero_promo_cta_button)

    def second_two_col_component_is_displayed(self):
        return self._is_displayed(self.second_two_col_component)

    def second_two_col_component_text_is_displayed(self):
        return self._is_displayed(self.second_two_col_component_text)

    def second_two_col_component_image_is_displayed(self):
        return self._is_displayed(self.second_two_col_component_image)

    def related_information_banner_is_displayed(self):
        return self._is_displayed(self.related_information_banner)

    def get_related_products_cards(self):
        cards = self.driver.find_elements_by_css_selector(
            'body > section.column-card-list.column-card-list--gray-back > div > div.cards > div')
        return cards

    def related_products_cards_count(self):
        return len(self.get_related_products_cards())

    def find_items(self, item):
        return self._find(item)