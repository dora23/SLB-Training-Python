from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class SearchFunctionality(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    search_field = {"by": By.CSS_SELECTOR,
                    "value": '#searchbox > div.CoveoOmnibox.coveo-query-syntax-disabled.magic-box > div.magic-box-input > input'}

    magnifying_glass = {"by": By.CSS_SELECTOR,
                        "value": '#searchbox > a'}

    searched_word = {"by": By.CSS_SELECTOR,
                     "value": '#slb-search > section > div > div.large-9.small-12.columns.filtered-rows__rows > span > span > span:nth-child(4)'}

    selected_option = {"by": By.CSS_SELECTOR,
                               "value": '#slb-search > section > div > div.large-9.small-12.columns.filtered-rows__rows > div:nth-child(3) > div > div.coveo-breadcrumb-items > div > span.coveo-facet-breadcrumb-values > div > span.coveo-facet-breadcrumb-caption'}

    results_nr = {"by": By.CSS_SELECTOR,
                  "value": '#slb-search > section > div > div.large-9.small-12.columns.filtered-rows__rows > span > span > span:nth-child(3)'}

    nr_of_results_displayed_product = {"by": By.CSS_SELECTOR,
                               "value": '#product-facet > ul > li > label > div > span.coveo-facet-value-count'}

    nr_of_results_displayed_content_type = {"by": By.CSS_SELECTOR,
                                       "value": '#template-facet > ul > li > label > div > span.coveo-facet-value-count'}

    nr_of_results_displayed_country = {"by": By.CSS_SELECTOR,
                                            "value": '#country-facet > ul > li > label > div > span.coveo-facet-value-count'}

    nr_of_results_displayed_challenge = {"by": By.CSS_SELECTOR,
                                            "value": '#challenge-facet > ul > li > label > div > span.coveo-facet-value-count'}

    nr_of_results_displayed_topic = {"by": By.CSS_SELECTOR,
                                            "value": '#topic-facet > ul > li > label > div > span.coveo-facet-value-count'}

    nr_of_results_displayed_year = {"by": By.CSS_SELECTOR,
                                            "value": '#year-facet > ul > li > label > div > span.coveo-facet-value-count'}

    clear_all_button = {"by": By.CSS_SELECTOR,
                        "value": 'div.coveo-breadcrumb-items > div > span.coveo-facet-breadcrumb-values > div > span.coveo-facet-breadcrumb-clear'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def select_product_option(self, product_option):
        product_option = self.driver.find_element_by_css_selector(
            '#product-facet > ul > li > label > div > span[data-original-value="' + product_option + '"]')
        product_option.click()

    def selected_option_get_text(self):
        return self._get_text(self.selected_option)

    def select_content_type_option(self, content_type):
        content_type = self.driver.find_element_by_css_selector(
            '#template-facet > ul > li > label > div > span[data-original-value="' + content_type + '"]')
        content_type.click()

    def select_country_option(self, country):
        country = self.driver.find_element_by_css_selector(
            '#country-facet > ul > li > label > div > span[data-original-value="' + country + '"]')
        country.click()

    def select_challenge_option(self, challenge):
        challenge = self.driver.find_element_by_css_selector(
            '#challenge-facet > ul > li > label > div > span[data-original-value="' + challenge + '"]')
        challenge.click()

    def select_topic_option(self, topic):
        topic = self.driver.find_element_by_css_selector(
            '#topic-facet > ul > li > label > div > span[data-original-value="' + topic + '"]')
        topic.click()

    def select_year_option(self, year):
        year = self.driver.find_element_by_css_selector(
            '#year-facet > ul > li > label > div > span[data-original-value="' + year + '"]')
        year.click()

    def fill_in_searched_word(self, word_to_search):
        self._click(self.search_field)
        self._type(self.search_field, word_to_search)
        self._click(self.magnifying_glass)

    def searched_word_get_text(self):
        return self._get_text(self.searched_word)

    def results_nr_get_text(self):
        return self._get_text(self.results_nr)

    def nr_of_results_displayed_product_get_text(self):
        return self._get_text(self.nr_of_results_displayed_product)

    def nr_of_results_displayed_content_type_get_text(self):
        return self._get_text(self.nr_of_results_displayed_content_type)

    def nr_of_results_displayed_country_get_text(self):
        return self._get_text(self.nr_of_results_displayed_country)

    def nr_of_results_displayed_challenge_get_text(self):
        return self._get_text(self.nr_of_results_displayed_challenge)

    def nr_of_results_displayed_topic_get_text(self):
        return self._get_text(self.nr_of_results_displayed_topic)

    def nr_of_results_displayed_year_get_text(self):
        return self._get_text(self.nr_of_results_displayed_year)

    def click_on_clear_all_button(self):
        self._click(self.clear_all_button)
