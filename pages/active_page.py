from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import active_slb_url


class ActivePage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    hero_section = {"by": By.CSS_SELECTOR,
                    "value": 'section.hero-section'}

    cta_banner = {"by": By.CSS_SELECTOR,
                  "value": '#ctabanner'}

    h1 = {"by": By.CSS_SELECTOR,
          "value": 'section.hero-section > div.hero-title > div.hero__title > h1'}

    h2 = {"by": By.CSS_SELECTOR,
          "value": 'section.hero-section > div.hero-title > div.hero__tagline > h2'}

    bread_crumbs = {"by": By.CSS_SELECTOR,
                    "value": 'div.breadcrumb__wrapper.absolute'}

    contact_us_cta = {"by": By.CSS_SELECTOR,
                      "value": '#ctabanner > div > div > div:nth-child(1)'}

    related_documents_cta = {"by": By.CSS_SELECTOR,
                             "value": '#ctabanner > div > div > div:nth-child(2)'}

    two_col_component = {"by": By.CSS_SELECTOR,
                             "value": 'div.content-two-col.rte-tables'}

    hero_promo = {"by": By.CSS_SELECTOR,
                         "value": 'section.hero-promo'}

    download_cta_button = {"by": By.CSS_SELECTOR,
                         "value": 'section.hero-promo > div > div.small-12.medium-7.large-7.columns.no-padd > div > a'}

    services_section = {"by": By.XPATH,
                  "value": '/html/body/section[4]/div/div[1]/div'}

    tools_section = {"by": By.XPATH,
                        "value": '/html/body/section[5]/div/div[1]/div'}

    view_all_related_information_cta = {"by": By.XPATH,
                        "value": '/html/body/section[6]/div/a'}

    selected_option = {"by": By.CSS_SELECTOR,
                                        "value": 'div.selected-options > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    def navigate_to_slb_active(self):
        self._visit(active_slb_url)

    def selected_option_get_text(self):
        return self._get_text(self.selected_option)

    def bread_crumbs_is_displayed(self):
        return self._is_displayed(self.bread_crumbs)

    def hero_section_is_displayed(self):
        return self._is_displayed(self.hero_section)

    def contact_us_cta_is_displayed(self):
        return self._is_displayed(self.contact_us_cta)

    def related_documents_cta_is_displayed(self):
        return self._is_displayed(self.related_documents_cta)

    def cta_banner_is_displayed(self):
        return self._is_displayed(self.cta_banner)

    def h1_get_text(self):
        return self._get_text(self.h1)

    def h2_get_text(self):
        return self._get_text(self.h2)

    def two_col_component_is_displayed(self):
        return self._is_displayed(self.two_col_component)

    def hero_promo_is_displayed(self):
        return self._is_displayed(self.hero_promo)

    def download_cta_button_is_displayed(self):
        return self._is_displayed(self.download_cta_button)

    def scroll_to_services_card(self):
        return self._scroll_to_element(self.services_section)

    def click_on_services_card(self):
        self._click(self.services_section)

    def click_on_tools_section(self):
        self._click(self.tools_section)

    def click_on_view_all_related_information_cta(self):
        self._click(self.view_all_related_information_cta)

    def get_services_cards(self):
        cards = self.driver.find_elements_by_xpath(
            '/html/body/section[4]/div/div[2]/div/section/div/div/div/div')
        return cards

    def services_cards_count(self):
        return len(self.get_services_cards())

    def find_items(self, item):
        return self._find(item)

    def get_tools_cards(self):
        cards = self.driver.find_elements_by_xpath(
            '/html/body/section[5]/div/div[2]/div/section/div/div/div/div')
        return cards

    def tools_cards_count(self):
        return len(self.get_tools_cards())

    def get_related_information_cards(self):
        cards = self.driver.find_elements_by_xpath(
            '/html/body/section[6]/div/div/div')
        return cards

    def related_information_cards_count(self):
        return len(self.get_related_information_cards())