import time

import pytest

from pages import home_page


class TestHomePage():
    @pytest.fixture
    def home(self, driver):
        return home_page.HomePage(driver)

    # Press Release Component

    def test_press_release_component(self, driver, home):
        home.navigate_to_slb()
        time.sleep(2)
        current_link = "https://www.slb.com/who-we-are/hse/covid-19"

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

    # Four Column Component

    def test_four_column_component(self, driver, home):
        four_column_component_1_link = 'https://www.slb.com/drilling/surface-and-downhole-logging/measurements-while-drilling-services/xbolt-g2-accelerated-drilling-service'
        four_column_component_2_link = 'https://www.slb.com/completions/well-completions/packers/blueplug-max-p-bridge-plug'
        four_column_component_3_link = 'https://www.slb.com/completions/stimulation/frac-and-flowback-equipment/valvecommander-platform'
        four_column_component_4_link = 'https://www.slb.com/well-intervention/coiled-tubing-intervention/active-real-time-downhole-coiled-tubing-services/active-power-ct-powered-measurements-system'

        home.navigate_to_slb()
        time.sleep(2)
        home.scroll_to_four_column_component()
        time.sleep(2)

        if home.four_column_component_is_displayed():
            if home.four_column_component_1_is_displayed():
                print("-------------------------------------------------")
                print(home.four_column_component_1_name_get_text())
                print(home.four_column_component_1_title_get_text())
                print(home.four_column_component_1_description_get_text())
                print("-------------------------------------------------")
                if home.four_column_component_1_image_is_displayed():
                    home.click_on_four_column_component_1_image()
                    time.sleep(2)
                    assert (four_column_component_1_link == home.get_current_link(), "The link has been changed")
                    home.navigate_to_slb()
                    time.sleep(2)
                    home.scroll_to_four_column_component()
                    time.sleep(2)
            else:
                print("The Component 1 is not displayed")

            if home.four_column_component_2_is_displayed():
                print(home.four_column_component_2_name_get_text())
                print(home.four_column_component_2_title_get_text())
                print(home.four_column_component_2_description_get_text())
                print("-------------------------------------------------")
                if home.four_column_component_2_image_is_displayed():
                    home.click_on_four_column_component_2_image()
                    time.sleep(2)
                    assert (four_column_component_2_link == home.get_current_link(), "The link has been changed")
                    home.navigate_to_slb()
                    time.sleep(2)
                    home.scroll_to_four_column_component()
                    time.sleep(2)
            else:
                print("The Component 2 is not displayed")

            if home.four_column_component_3_is_displayed():
                print(home.four_column_component_3_name_get_text())
                print(home.four_column_component_3_title_get_text())
                print(home.four_column_component_3_description_get_text())
                print("-------------------------------------------------")
                if home.four_column_component_3_image_is_displayed():
                    home.click_on_four_column_component_3_image()
                    time.sleep(2)
                    assert (four_column_component_3_link == home.get_current_link(), "The link has been changed")
                    home.navigate_to_slb()
                    time.sleep(2)
                    home.scroll_to_four_column_component()
                    time.sleep(2)
            else:
                print("The Component 3 is not displayed")

            if home.four_column_component_4_is_displayed():
                print(home.four_column_component_4_name_get_text())
                print(home.four_column_component_4_title_get_text())
                print(home.four_column_component_4_description_get_text())
                print("-------------------------------------------------")
                if home.four_column_component_4_image_is_displayed():
                    home.click_on_four_column_component_4_image()
                    time.sleep(2)
                    assert (four_column_component_4_link == home.get_current_link(), "The link has been changed")
            else:
                print("The Component 4 is not displayed")
        else:
            print("The Four Column Component Is Not Displayed")

    # Full Width Promo Component

    def test_full_width_promo_component(self, driver, home):
        cta_button_link = 'https://connect.slb.com/register'

        home.navigate_to_slb()
        time.sleep(2)
        home.scroll_to_full_width_promo_component()
        time.sleep(2)

        if home.full_width_promo_component_is_displayed():
            print(home.full_width_promo_component_title_get_text())
            print(home.full_width_promo_component_description_get_text())
            print(home.full_width_promo_component_list_item_1_get_text())
            print(home.full_width_promo_component_list_item_2_get_text())
            print(home.full_width_promo_component_list_item_3_get_text())
            print(home.full_width_promo_component_list_item_4_get_text())
            if home.full_width_promo_component_cta_button_is_displayed():
                home.click_on_full_width_promo_component_cta_button()
                time.sleep(2)
                assert (cta_button_link == home.get_current_link())
            else:
                print("The link has been changed")
        else:
            print("The Full Width Promo Component Is Not Displayed")

    # Four Column Promo Interview Component

    def test_promo_interview_component(self, driver, home):

        home.navigate_to_slb()
        time.sleep(2)
        home.scroll_to_promo_interview_component()
        time.sleep(2)

        if home.promo_interview_component_is_displayed():
            print(home.promo_interview_name_1_get_text())
            print(home.promo_interview_title_1_get_text())
            print(home.promo_interview_description_1_get_text())
            assert home.promo_interview_image_1_is_displayed()
            print("-------------------------------------------------")
            print(home.promo_interview_name_2_get_text())
            print(home.promo_interview_title_2_get_text())
            print(home.promo_interview_description_2_get_text())
            assert home.promo_interview_image_2_is_displayed()
            print("------------------------------------------------~-"
                  "++++++++++++++++++++++-")
            print(home.promo_interview_name_3_get_text())
            print(home.promo_interview_title_3_get_text())
            print(home.promo_interview_description_3_get_text())
            assert home.promo_interview_image_3_is_displayed()
            print("-------------------------------------------------")
            print(home.promo_interview_name_4_get_text())
            print(home.promo_interview_title_4_get_text())
            print(home.promo_interview_description_4_get_text())
            assert home.promo_interview_image_4_is_displayed()
        else:
            print("The Promo Interview Component Is Not Displayed")
