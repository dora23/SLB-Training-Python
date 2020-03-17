import time

import pytest

from pages import home_page


class TestHomePage():
    @pytest.fixture
    def home(self, driver):
        return home_page.HomePage(driver)

    def test_press_release_component(self, driver, home):
        home.navigate_to_slb()
        time.sleep(2)
        current_link = "https://www.slb.com/who-we-are/hse/covid-179"

        if home.press_release_component_is_displayed():
            print(home.press_release_1_get_date() + '  ' + home.press_release_1_get_text())
            print(home.press_release_2_get_date() + '  ' + home.press_release_2_get_text())
            print(home.press_release_3_get_date() + '  ' + home.press_release_3_get_text())
            if home.callout_component_is_displayed():
                print(home.callout_component_title_get_text())
                print(home.callout_component_description_get_text())
                if home.callout_component_cta_button_is_displayed():
                    home.click_on_callout_component_cta_button()
                    time.sleep(2)
                    if current_link == home.return_current_url():
                        print("The link is correct")
                    else:
                        print("The link has been changed")
                else:
                    print("The CTA button is not displayed")
            else:
                print("The callout component is not available")

        else:
            print("The press release component is not present on the page")
