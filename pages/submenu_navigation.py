from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class SubmenuPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    submenu_bar = {"by": By.CSS_SELECTOR, "value": 'div.wrapper.show-for-large'}
    submenu_chr = {"by": By.CSS_SELECTOR, "value": '#mainnav__511e3bf8-27cb-4a88-8220-9f3df25c08c9 >a'}
    submenu_drill = {"by": By.CSS_SELECTOR, "value": '#mainnav__b21fea09-dbc0-4d39-ab1c-eabfe3b791e6 > a'}
    submenu_comp = {"by": By.CSS_SELECTOR, "value": '#mainnav__2cc866ee-53dd-409d-8dbf-83e025535d5e > a'}
    submenu_prod = {"by": By.CSS_SELECTOR, "value": '#mainnav__027c1327-8430-4224-aedb-b9b131f0a322 > a'}
    submenu_interv = {"by": By.CSS_SELECTOR, "value": '#mainnav__1962fc28-6344-4d17-bde0-5aca4c6e61a2 > a'}
    submenu_insights = {"by": By.CSS_SELECTOR,
                        "value": 'div.wrapper.show-for-large > div.primary-navigation__container > ul.sub-nav > li:nth-child(1) > a'}
    submenu_resource = {"by": By.CSS_SELECTOR,
                        "value": 'div.wrapper.show-for-large > div.primary-navigation__container > ul.sub-nav > li:nth-child(2) > a'}
    submenu_location = {"by": By.CSS_SELECTOR,
                        "value": 'div.wrapper.show-for-large > div.primary-navigation__container > ul.sub-nav > li:nth-child(3) > a'}
    submenu_soft = {"by": By.CSS_SELECTOR,
                    "value": 'div.wrapper.show-for-large > div.primary-navigation__container > ul.sub-nav > li:nth-child(4) > a'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def submenu_bar_is_displayed(self):
        return self._is_displayed(self.submenu_bar)

    def submenu_chr_get_text(self):
        return self._get_text(self.submenu_chr)

    def submenu_dril_get_text(self):
        return self._get_text(self.submenu_drill)

    def submenu_comp_get_text(self):
        return self._get_text(self.submenu_comp)

    def submenu_prod_get_text(self):
        return self._get_text(self.submenu_prod)

    def submenu_interv_get_text(self):
        return self._get_text(self.submenu_interv)

    def submenu_insights_get_text(self):
        return self._get_text(self.submenu_insights)

    def submenu_resource_get_text(self):
        return self._get_text(self.submenu_resource)

    def submenu_location_get_text(self):
        return self._get_text(self.submenu_location)

    def submenu_soft_get_text(self):
        return self._get_text(self.submenu_soft)

    def click_on_submenu_chr(self):
        self._click(self.submenu_chr)

    def click_on_submenu_drill(self):
        self._click(self.submenu_drill)

    def click_on_submenu_completion(self):
        self._click(self.submenu_comp)

    def click_on_submenu_prod(self):
        self._click(self.submenu_prod)

    def click_on_submenu_interv(self):
        self._click(self.submenu_interv)

    def get_characterization_submenu_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#mega__511e3bf8-27cb-4a88-8220-9f3df25c08c9 > div.row > div.megamenu__main > div.megamenu__main__col')
        return elems

    def characterization_submenu_items_count(self):
        return len(self.get_characterization_submenu_items())

    def find_items(self, item):
        return self._find(item)

    def get_drill_submenu_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#mega__b21fea09-dbc0-4d39-ab1c-eabfe3b791e6 > div.row > div.megamenu__main > div.megamenu__main__col')
        return elems

    def drill_submenu_items_count(self):
        return len(self.get_drill_submenu_items())

    def get_completion_submenu_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#mega__2cc866ee-53dd-409d-8dbf-83e025535d5e > div.row > div.megamenu__main > div.megamenu__main__col')
        return elems

    def completion_submenu_items_count(self):
        return len(self.get_completion_submenu_items())

    def get_production_submenu_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#mega__027c1327-8430-4224-aedb-b9b131f0a322 > div.row > div.megamenu__main > div.megamenu__main__col')
        return elems

    def production_submenu_items_count(self):
        return len(self.get_production_submenu_items())

    def get_intervention_submenu_items(self):
        elems = self.driver.find_elements_by_css_selector(
            '#mega__1962fc28-6344-4d17-bde0-5aca4c6e61a2 > div.row > div.megamenu__main > div.megamenu__main__col')
        return elems

    def intervention_submenu_items_count(self):
        return len(self.get_intervention_submenu_items())