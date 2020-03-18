from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class HomePage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    # Press Releases Component
    press_release_component = {"by": By.CSS_SELECTOR, "value": 'section.multi-col-press-release'}
    press_release_1_date = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(1) > div'}
    press_release_1_text = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(1) > h3 > a'}
    press_release_2_date = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(2) > div'}
    press_release_2_text = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(2) > h3 > a'}
    press_release_3_date = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(3) > div'}
    press_release_3_text = {"by": By.CSS_SELECTOR,
                            "value": 'section.multi-col-press-release > div > div > div:nth-child(3) > h3 > a'}
    callout_component = {"by": By.CSS_SELECTOR,
                         "value": 'div.multi-col-press-release__item.callout-wrapper.medium-6.small-12.large-3 > div'}
    callout_component_title = {"by": By.CSS_SELECTOR,
                               "value": 'div.multi-col-press-release__item.callout-wrapper.medium-6.small-12.large-3 > div > div.title'}

    callout_component_description = {"by": By.CSS_SELECTOR,
                                     "value": 'div.multi-col-press-release__item.callout-wrapper.medium-6.small-12.large-3 > div > div.desc'}

    callout_component_cta_button = {"by": By.CSS_SELECTOR,
                                    "value": 'div.multi-col-press-release__item.callout-wrapper.medium-6.small-12.large-3 > div > a'}

    # --------------------------------------------------------------------------------------------------------------------------------
    # Four Column Promo Component

    four_column_component = {"by": By.CSS_SELECTOR, "value": 'body > section:nth-child(5)'}

    four_column_component_1 = {"by": By.CSS_SELECTOR,
                               "value": 'section:nth-child(4) > div > div > ul > li:nth-child(1)'}

    four_column_component_1_image = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(1) > a'}
    four_column_component_1_name = {"by": By.CSS_SELECTOR,
                                    "value": 'section:nth-child(4) > div > div > ul > li:nth-child(1) > div > a > h3'}
    four_column_component_1_title = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(1) > div > h4'}
    four_column_component_1_description = {"by": By.CSS_SELECTOR,
                                           "value": 'section:nth-child(4) > div > div > ul > li:nth-child(1) > div > p'}
    four_column_component_2 = {"by": By.CSS_SELECTOR,
                               "value": 'section:nth-child(4) > div > div > ul > li:nth-child(2)'}

    four_column_component_2_image = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(2) > a'}
    four_column_component_2_name = {"by": By.CSS_SELECTOR,
                                    "value": 'section:nth-child(4) > div > div > ul > li:nth-child(2) > div > a > h3'}
    four_column_component_2_title = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(2) > div > h4'}
    four_column_component_2_description = {"by": By.CSS_SELECTOR,
                                           "value": 'section:nth-child(4) > div > div > ul > li:nth-child(2) > div > p'}
    four_column_component_3 = {"by": By.CSS_SELECTOR,
                               "value": 'section:nth-child(4) > div > div > ul > li:nth-child(3)'}

    four_column_component_3_image = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(3) > a'}
    four_column_component_3_name = {"by": By.CSS_SELECTOR,
                                    "value": 'section:nth-child(4) > div > div > ul > li:nth-child(3) > div > a > h3'}
    four_column_component_3_title = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(3) > div > h4'}
    four_column_component_3_description = {"by": By.CSS_SELECTOR,
                                           "value": 'section:nth-child(4) > div > div > ul > li:nth-child(3) > div > p'}
    four_column_component_4 = {"by": By.CSS_SELECTOR,
                               "value": 'section:nth-child(4) > div > div > ul > li:nth-child(4)'}

    four_column_component_4_image = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(4) > a'}
    four_column_component_4_name = {"by": By.CSS_SELECTOR,
                                    "value": 'section:nth-child(4) > div > div > ul > li:nth-child(4) > div > a > h3'}
    four_column_component_4_title = {"by": By.CSS_SELECTOR,
                                     "value": 'section:nth-child(4) > div > div > ul > li:nth-child(4) > div > h4'}
    four_column_component_4_description = {"by": By.CSS_SELECTOR,
                                           "value": 'section:nth-child(4) > div > div > ul > li:nth-child(4) > div > p'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def press_release_component_is_displayed(self):
        return self._is_displayed(self.press_release_component)

    def press_release_1_get_date(self):
        return self._get_text(self.press_release_1_date)

    def press_release_1_get_text(self):
        return self._get_text(self.press_release_1_text)

    def press_release_2_get_date(self):
        return self._get_text(self.press_release_2_date)

    def press_release_2_get_text(self):
        return self._get_text(self.press_release_2_text)

    def press_release_3_get_date(self):
        return self._get_text(self.press_release_3_date)

    def press_release_3_get_text(self):
        return self._get_text(self.press_release_3_text)

    def callout_component_is_displayed(self):
        return self._is_displayed(self.callout_component)

    def callout_component_title_get_text(self):
        return self._get_text(self.callout_component_title)

    def callout_component_description_get_text(self):
        return self._get_text(self.callout_component_description)

    def callout_component_cta_button_is_displayed(self):
        return self._is_displayed(self.callout_component_cta_button)

    def click_on_callout_component_cta_button(self):
        self._click(self.callout_component_cta_button)

    def return_current_url(self):
        return self._get_current_url()

    # --------------------------------------------------------------------------------------------------------------------------------
    # Four Column Promo Component
    def scroll_to_four_column_component(self):
        return self._scroll_to_element(self.four_column_component)

    def four_column_component_is_displayed(self):
        return self._is_displayed(self.four_column_component)

    def four_column_component_1_is_displayed(self):
        return self._is_displayed(self.four_column_component_1)

    def four_column_component_2_is_displayed(self):
        return self._is_displayed(self.four_column_component_2)

    def four_column_component_3_is_displayed(self):
        return self._is_displayed(self.four_column_component_3)

    def four_column_component_4_is_displayed(self):
        return self._is_displayed(self.four_column_component_4)

    def four_column_component_1_image_is_displayed(self):
        return self._is_displayed(self.four_column_component_1_image)

    def four_column_component_2_image_is_displayed(self):
        return self._is_displayed(self.four_column_component_2_image)

    def four_column_component_3_image_is_displayed(self):
        return self._is_displayed(self.four_column_component_3_image)

    def four_column_component_4_image_is_displayed(self):
        return self._is_displayed(self.four_column_component_4_image)

    def four_column_component_1_name_get_text(self):
        return self._get_text(self.four_column_component_1_name)

    def four_column_component_2_name_get_text(self):
        return self._get_text(self.four_column_component_2_name)

    def four_column_component_3_name_get_text(self):
        return self._get_text(self.four_column_component_3_name)

    def four_column_component_4_name_get_text(self):
        return self._get_text(self.four_column_component_4_name)

    def four_column_component_1_title_get_text(self):
        return self._get_text(self.four_column_component_1_title)

    def four_column_component_2_title_get_text(self):
        return self._get_text(self.four_column_component_2_title)

    def four_column_component_3_title_get_text(self):
        return self._get_text(self.four_column_component_3_title)

    def four_column_component_4_title_get_text(self):
        return self._get_text(self.four_column_component_4_title)

    def four_column_component_1_description_get_text(self):
        return self._get_text(self.four_column_component_1_description)

    def four_column_component_2_description_get_text(self):
        return self._get_text(self.four_column_component_2_description)

    def four_column_component_3_description_get_text(self):
        return self._get_text(self.four_column_component_3_description)

    def four_column_component_4_description_get_text(self):
        return self._get_text(self.four_column_component_4_description)

    def get_current_link(self):
        return self._get_current_url()

    def click_on_four_column_component_1_image(self):
        self._click(self.four_column_component_1_image)

    def click_on_four_column_component_2_image(self):
        self._click(self.four_column_component_2_image)

    def click_on_four_column_component_3_image(self):
        self._click(self.four_column_component_3_image)

    def click_on_four_column_component_4_image(self):
        self._click(self.four_column_component_4_image)