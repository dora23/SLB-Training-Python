import self as self
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl, insightsurl


class InsightsPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    insights_menu_option = {"by": By.CSS_SELECTOR,
                            "value": 'div.primary-navigation__container > ul.sub-nav > li:nth-child(1) > a'}

    hero_section = {"by": By.CSS_SELECTOR,
                    "value": 'section.hero-carousel > div > div.owl-stage-outer > div > div.owl-item.active > div'}

    hero_title = {"by": By.CSS_SELECTOR,
                  "value": 'div.owl-stage-outer > div > div.owl-item.active > div > div.row.no-padd > div > div > div.herobox__title'}

    hero_subtitle = {"by": By.CSS_SELECTOR,
                     "value": 'div.owl-item.active > div > div.row.no-padd > div > div > div.herobox__subtitle'}

    hero_cta_button = {"by": By.CSS_SELECTOR,
                       "value": 'div.owl-item.active > div > div.row.no-padd > div > div > div.herobox__cta > a'}

    load_more_button = {"by": By.CSS_SELECTOR,
                        "value": 'div.tiles__wrapper > div.tiles__load-more > button'}

    well_phase_option = {"by": By.CSS_SELECTOR,
                         "value": 'div.browse-by__menus.show-for-medium > div > div:nth-child(1) > div.accordion-filters__menu__toggle > button'}

    well_phase_selected_option = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__selected-options > div > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    trending_topic_option = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__menus.show-for-medium > div > div:nth-child(2) > div.accordion-filters__menu__toggle > button'}

    trending_topic_selected_option = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__selected-options > div > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    type_option = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__menus.show-for-medium > div > div:nth-child(3) > div.accordion-filters__menu__toggle > button'}

    type_option_selected_option = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__selected-options > div > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}


    clear_all_button = {"by": By.CSS_SELECTOR,
                                  "value": 'div.browse-by__selected-options > div > div.selected-options__items > div.selected-options__clear-items > button'}


    def select_well_phase_option(self, well_phase_option):
        well_phase_option = self.driver.find_element_by_css_selector(
            'div.browse-by__menus.show-for-medium > div > div.accordion-filters__menu.toggle > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + well_phase_option + '"]')
        well_phase_option.click()

    def select_trending_topic_option(self, trending_topic_option):
        trending_topic_option = self.driver.find_element_by_css_selector(
            'div.accordion-filters__menu.toggle > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + trending_topic_option +'"]')
        trending_topic_option.click()

    def select_type_option_option(self, type_option):
        type_option = self.driver.find_element_by_css_selector(
            'div.accordion-filters__menu.toggle > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + type_option +'"]')
        type_option.click()

    def navigate_to_slb(self):
        self._visit(baseurl)

    def navigate_to_insightsurl(self):
        self._visit(insightsurl)

    def click_on_load_more_button(self):
        self._click(self.load_more_button)

    def click_on_insights_menu_option(self):
        self._click(self.insights_menu_option)

    def click_on_trending_topic_option(self):
        self._click(self.trending_topic_option)

    def click_on_well_phase_option(self):
        self._click(self.well_phase_option)

    def click_on_type_option(self):
        self._click(self.type_option)

    def click_on_hero_cta_button(self):
        self._click(self.hero_cta_button)

    def load_more_button_is_displayed(self):
        return self._is_displayed(self.load_more_button)

    def hero_section_is_displayed(self):
        return self._is_displayed(self.hero_section)

    def hero_title_get_text(self):
        return self._get_text(self.hero_title)

    def hero_subtitle_get_text(self):
        return self._get_text(self.hero_subtitle)

    def return_current_url(self):
        return self._get_current_url()

    def hero_cta_button_is_displayed(self):
        return self._is_displayed(self.hero_cta_button)

    def get_article_cards(self):
        cards = self.driver.find_elements_by_css_selector(
            'div.tiles__wrapper > div.tiles > div')
        return cards

    def article_cards_count(self):
        return len(self.get_article_cards())

    def find_items(self, item):
        return self._find(item)

    def well_phase_selected_option_get_text(self):
        return self._get_text(self.well_phase_selected_option)

    def click_on_clear_all_button(self):
        self._click(self.clear_all_button)

    def trending_topic_selected_option_get_text(self):
        return self._get_text(self.trending_topic_selected_option)

    def type_option_selected_option_get_text(self):
        return self._get_text(self.type_option_selected_option)