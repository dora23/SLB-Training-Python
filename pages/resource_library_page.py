from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import resourceurl


class ResourceLibraryPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    clear_all_button = {"by": By.CSS_SELECTOR,
                        "value": 'div.selected-options > div.selected-options__items > div.selected-options__clear-items > button'}

    # Topic Filter

    topic_menu = {"by": By.CSS_SELECTOR,
                  "value": 'div.show-for-large > div > div:nth-child(1) > div.accordion-filters__menu__toggle > button'}
    topic_selected_option = {"by": By.CSS_SELECTOR,
                             "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    # Section Filter

    section_menu = {"by": By.CSS_SELECTOR,
                    "value": 'div.show-for-large > div > div:nth-child(2) > div.accordion-filters__menu__toggle > button'}

    section_selected_option = {"by": By.CSS_SELECTOR,
                               "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item > span:nth-child(2)'}

    section2_selected_option = {"by": By.CSS_SELECTOR,
                               "value": 'div.selected-options > div.selected-options__items > div:nth-child(2) > span:nth-child(2)'}
    # Product Name Filter

    product_name_menu = {"by": By.CSS_SELECTOR,
                         "value": 'div.show-for-large > div > div:nth-child(3) > div.accordion-filters__menu__toggle > button'}

    product_name_selected_option = {"by": By.CSS_SELECTOR,
                                    "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item > span:nth-child(1)'}
    show_more_products = {"by": By.CSS_SELECTOR,
                          "value": 'div.show-for-large > div > div.accordion-filters__menu.toggle > div.accordion-filters__menu__list.display > button'}

    # Resource Type Filter

    resource_type_menu = {"by": By.CSS_SELECTOR,
                          "value": 'div.show-for-large > div > div:nth-child(4) > div.accordion-filters__menu__toggle > button'}

    resource_type_selected_option = {"by": By.CSS_SELECTOR,
                                     "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item'}

    # Country Filter

    country_menu = {"by": By.CSS_SELECTOR,
                    "value": 'div.show-for-large > div > div:nth-child(5) > div.accordion-filters__menu__toggle > button'}

    country_selected_option = {"by": By.CSS_SELECTOR,
                               "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item'}

    # Region Filter

    region_menu = {"by": By.CSS_SELECTOR,
                   "value": 'div.show-for-large > div > div:nth-child(6) > div.accordion-filters__menu__toggle > button'}

    region_selected_option = {"by": By.CSS_SELECTOR,
                              "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item'}

    # State Filter

    state_menu = {"by": By.CSS_SELECTOR,
                  "value": 'div.show-for-large > div > div:nth-child(7) > div.accordion-filters__menu__toggle > button'}

    state_selected_option = {"by": By.CSS_SELECTOR,
                             "value": 'div.large-3.small-12.columns.filtered-rows__filters > div.show-for-large > div > div.accordion-filters__menu.toggle > div.accordion-filters__menu__list.display > div > label:nth-child(3) > input[type=checkbox]'}

    # Year Filter

    year_menu = {"by": By.CSS_SELECTOR,
                 "value": 'div.show-for-large > div > div:nth-child(8) > div.accordion-filters__menu__toggle > button'}

    year_selected_option = {"by": By.CSS_SELECTOR,
                            "value": 'div.large-9.small-12.columns.filtered-rows__rows > div > div.selected-options > div.selected-options__items > div.selected-options__item'}

    def navigate_to_slb(self):
        self._visit(resourceurl)

    def click_on_clear_all_button(self):
        self._click(self.clear_all_button)

    # Topic Filter

    def click_on_topic_menu(self):
        self._click(self.topic_menu)

    def select_topic_option(self, topic_option):
        topic_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(1) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + topic_option + '"]')
        topic_option.click()



    def topic_selected_option_get_text(self):
        return self._get_text(self.topic_selected_option)

    # Section Filter

    def click_on_section_menu(self):
        self._click(self.section_menu)

    def select_section_option(self, section_option):
        section_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(2) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + section_option + '"]')
        section_option.click()

    def section_selected_option_get_text(self):
        return self._get_text(self.section_selected_option)

    def section2_selected_option_get_text(self):
        return self._get_text(self.section2_selected_option)

    # Product Name Filter

    def click_on_product_name_menu(self):
        self._click(self.product_name_menu)

    def select_product_name_option(self, product_name_option):
        product_name_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(3) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + product_name_option + '"]')
        product_name_option.click()

    def product_name_selected_option_get_text(self):
        return self._get_text(self.product_name_selected_option)

    def click_on_show_more_products(self):
        self._click(self.show_more_products)

    # Resource Type Filter

    def click_on_resource_type_menu(self):
        self._click(self.resource_type_menu)

    def select_resource_type_option(self, resource_type_option):
        resource_type_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(4) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + resource_type_option + '"]')
        resource_type_option.click()

    def resource_type_selected_option_get_text(self):
        return self._get_text(self.resource_type_selected_option)

    # Country Filter

    def click_on_country_menu(self):
        self._click(self.country_menu)

    def select_country_option(self, country_option):
        country_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(5) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + country_option + '"]')
        country_option.click()

    def country_selected_option_get_text(self):
        return self._get_text(self.country_selected_option)

    # Region Filter

    def click_on_region_menu(self):
        self._click(self.region_menu)

    def select_region_option(self, region_option):
        region_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(6) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + region_option + '"]')
        region_option.click()

    def region_selected_option_get_text(self):
        return self._get_text(self.region_selected_option)

    # State Filter

    def click_on_state_menu(self):
        self._click(self.state_menu)

    def select_state_option(self, state_option):
        state_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(7) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + state_option + '"]')
        state_option.click()

    def state_selected_option_get_text(self):
        return self._get_text(self.state_selected_option)

    # Year Filter

    def click_on_year_menu(self):
        self._click(self.year_menu)

    def select_year_option(self, year_option):
        year_option = self.driver.find_element_by_css_selector(
            'div.show-for-large > div > div:nth-child(8) > div.accordion-filters__menu__list.display > div > label > input[data-ajax-filter-name="' + year_option + '"]')
        year_option.click()

    def year_selected_option_get_text(self):
        return self._get_text(self.year_selected_option)
