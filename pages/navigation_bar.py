from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class NavigationBar(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    navigation_bar = {"by": By.CLASS_NAME, "value": "primary-navigation__container"}
    characterization = {"by": By.CSS_SELECTOR, "value": "#mainnav__511e3bf8-27cb-4a88-8220-9f3df25c08c9 > a"}
    drilling = {"by": By.CSS_SELECTOR, "value": "#mainnav__b21fea09-dbc0-4d39-ab1c-eabfe3b791e6 > a"}
    completions = {"by": By.CSS_SELECTOR, "value": "#mainnav__2cc866ee-53dd-409d-8dbf-83e025535d5e > a"}
    production = {"by": By.CSS_SELECTOR, "value": "#mainnav__027c1327-8430-4224-aedb-b9b131f0a322 > a"}
    intervention = {"by": By.CSS_SELECTOR, "value": "#mainnav__1962fc28-6344-4d17-bde0-5aca4c6e61a2"}
    insights = {"by": By.CSS_SELECTOR, "value": "div.primary-navigation__container > ul.sub-nav > li:nth-child(1) > a"}
    resource_library = {"by": By.CSS_SELECTOR,
                        "value": "div.primary-navigation__container > ul.sub-nav > li:nth-child(2) > a"}
    locations = {"by": By.CSS_SELECTOR, "value": "div.primary-navigation__container > ul.sub-nav > li:nth-child(3) > a"}
    software = {"by": By.CSS_SELECTOR, "value": "div.primary-navigation__container > ul.sub-nav > li:nth-child(4) > a"}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def navigation_bar_is_displayed(self):
        return self._is_displayed(self.navigation_bar)

    def characterization_is_displayed(self):
        return self._is_displayed(self.characterization)

    def drilling_is_displayed(self):
        return self._is_displayed(self.drilling)

    def completions_is_displayed(self):
        return self._is_displayed(self.completions)

    def production_is_displayed(self):
        return self._is_displayed(self.production)

    def intervention_is_displayed(self):
        return self._is_displayed(self.intervention)

    def insights_is_displayed(self):
        return self._is_displayed(self.insights)

    def resource_library_is_displayed(self):
        return self._is_displayed(self.resource_library)

    def locations_is_displayed(self):
        return self._is_displayed(self.locations)

    def software_is_displayed(self):
        return self._is_displayed(self.software)