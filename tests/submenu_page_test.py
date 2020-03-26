import time

import pytest
from selenium.webdriver.common.by import By

from pages import submenu_page


class TestSubmenuPage():
    @pytest.fixture
    def submenu(self, driver):
        return submenu_page.SubmenuPage(driver)

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

    def test_submenu_title_text(self, driver, submenu):
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
