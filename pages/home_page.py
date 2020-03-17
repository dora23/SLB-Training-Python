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

    four_col_component = {"by": By.CSS_SELECTOR, "value": 'section.multi-col-press-release'}
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
