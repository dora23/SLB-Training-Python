import time

import pytest
from selenium.webdriver.common.by import By

from pages import submenu_navigation


class TestSubmenuPage():
    @pytest.fixture
    def submenu(self, driver):
        return submenu_navigation.SubmenuPage(driver)

    def test_sub_menu_bar(self, driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)

        if submenu.submenu_bar_is_displayed():
            print(submenu.submenu_chr_get_text())
            print(submenu.submenu_dril_get_text())
            print(submenu.submenu_comp_get_text())
            print(submenu.submenu_prod_get_text())
            print(submenu.submenu_interv_get_text())
            print(submenu.submenu_insights_get_text())
            print(submenu.submenu_resource_get_text())
            print(submenu.submenu_location_get_text())
            print(submenu.submenu_soft_get_text())

        else:
            print("Submenu bar is not displayed")

    def test_characterization_links(self, driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)
        submenu.click_on_submenu_chr()
        time.sleep(3)

        number_of_characterization_submenus = submenu.characterization_submenu_items_count()

        for x in range(1, number_of_characterization_submenus + 1):
            print("--------------------------------------")
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#mega__511e3bf8-27cb-4a88-8220-9f3df25c08c9 > div.row > div.megamenu__main > div.megamenu__main__col:nth-child(" + str(
                           x) + " ) "}
            submenu_item_titles = submenu.find_items(locator)
            print("\n" + submenu_item_titles.text)

    def test_drilling_links(self,driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)
        submenu.click_on_submenu_drill()
        time.sleep(3)

        number_of_drill_submenus = submenu.drill_submenu_items_count()

        for z in range(1, number_of_drill_submenus + 1):
            print("--------------------------------------")
            locator_drill = {"by": By.CSS_SELECTOR,
                   "value": "#mega__b21fea09-dbc0-4d39-ab1c-eabfe3b791e6 > div.row > div.megamenu__main > div.megamenu__main__col:nth-child(" + str(
                       z) + " ) "}
            submenu_item_titles = submenu.find_items(locator_drill)
            print("\n" + submenu_item_titles.text)

    def test_completion_links(self,driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)
        submenu.click_on_submenu_completion()
        time.sleep(3)

        number_of_completion_submenus = submenu.completion_submenu_items_count()

        for z in range(1, number_of_completion_submenus + 1):
            print("--------------------------------------")
            locator_completion = {"by": By.CSS_SELECTOR,
                   "value": "#mega__2cc866ee-53dd-409d-8dbf-83e025535d5e > div.row > div.megamenu__main > div.megamenu__main__col:nth-child(" + str(
                       z) + " ) "}
            submenu_item_titles = submenu.find_items(locator_completion)
            print("\n" + submenu_item_titles.text)

    def test_production_links(self,driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)
        submenu.click_on_submenu_prod()
        time.sleep(3)

        number_of_production_submenus = submenu.production_submenu_items_count()

        for z in range(1, number_of_production_submenus + 1):
            print("--------------------------------------")
            locator_production = {"by": By.CSS_SELECTOR,
                   "value": "#mega__027c1327-8430-4224-aedb-b9b131f0a322 > div.row > div.megamenu__main > div.megamenu__main__col:nth-child(" + str(
                       z) + " ) "}
            submenu_item_titles = submenu.find_items(locator_production)
            print("\n" + submenu_item_titles.text)

    def test_intervention_links(self,driver, submenu):
        submenu.navigate_to_slb()
        time.sleep(3)
        submenu.click_on_submenu_interv()
        time.sleep(3)

        number_of_intervention_submenus = submenu.production_submenu_items_count()

        for z in range(1, number_of_intervention_submenus + 1):
            print("--------------------------------------")
            locator_intervention = {"by": By.CSS_SELECTOR,
                   "value": "#mega__1962fc28-6344-4d17-bde0-5aca4c6e61a2 > div.row > div.megamenu__main > div.megamenu__main__col:nth-child(" + str(
                       z) + " ) "}
            submenu_item_titles = submenu.find_items(locator_intervention)
            print("\n" + submenu_item_titles.text)