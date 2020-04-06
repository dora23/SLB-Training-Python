import time

import pytest
from selenium.webdriver.common.by import By

from pages import active_page


class TestActivePage():
    @pytest.fixture
    def active(self, driver):
        return active_page.ActivePage(driver)

    def test_active_page(self, driver, active):
        active.navigate_to_slb_active()
        time.sleep(2)

        if active.hero_section_is_displayed:
            print(active.h1_get_text())
            print(active.h2_get_text())
            assert (active.bread_crumbs_is_displayed(), "The breadcrumbs are not displayed")
        else:
            print("The Hero Section is not displayed")

        if active.cta_banner_is_displayed():
            assert (active.contact_us_cta_is_displayed(), "The Contact Us cta button is not displayed")
            assert (active.related_documents_cta_is_displayed(), "The Related Documents cta button is not displayed")
        else:
            print("CTA banner is not displayed")

        assert (active.two_col_component_is_displayed(), "The Two Column component is not displayed")

        if active.hero_promo_is_displayed():
            assert (active.download_cta_button_is_displayed(), "The CTA button is not displayed")
        else:
            print("The Hero Promo section is not displayed")

    def test_active_page_cards(self, driver, active):
        active.navigate_to_slb_active()
        time.sleep(2)

        active.click_on_services_card()
        time.sleep(2)
        print(active.services_cards_count())

        number_of_card_items = active.services_cards_count()

        for x in range(1, number_of_card_items + 1):
            locator_title = {"by": By.XPATH,
                             "value": "/html/body/section[4]/div/div[2]/div/section/div/div/div/div[(" + str(
                                 x) + ")]/div/div[2]/h2/a"}
            locator_sub_title = {"by": By.XPATH,
                                 "value": "/html/body/section[4]/div/div[2]/div/section/div/div/div/div[(" + str(
                                     x) + ")]/div/div[2]/h3"}

            locator_description = {"by": By.XPATH,
                                   "value": "/html/body/section[4]/div/div[2]/div/section/div/div/div/div[(" + str(
                                       x) + ")]/div/div[2]/p"}

            card_titles = active.find_items(locator_title)
            card_sub_title = active.find_items(locator_sub_title)
            card_description = active.find_items(locator_description)
            print("\n" + card_titles.text + "\n" + card_sub_title.text + "\n" + card_description.text)
            print("-----------------------------------")

        active.click_on_services_card()
        time.sleep(1)

        active.click_on_tools_section()
        time.sleep(1)

        number_of_tools_card_items = active.tools_cards_count()

        for z in range(1, number_of_tools_card_items + 1):
            locator_title_tools = {"by": By.XPATH,
                                   "value": "/html/body/section[5]/div/div[2]/div/section/div/div/div/div[(" + str(
                                       z) + ")]/div/div[2]/h2/a"}
            locator_sub_title_tools = {"by": By.XPATH,
                                       "value": "/html/body/section[5]/div/div[2]/div/section/div/div/div/div[(" + str(
                                           z) + ")]/div/div[2]/h3"}

            locator_description_tools = {"by": By.XPATH,
                                         "value": "/html/body/section[5]/div/div[2]/div/section/div/div/div/div[(" + str(
                                             z) + ")]/div/div[2]/p"}

            card_titles_tools = active.find_items(locator_title_tools)
            card_sub_title_tools = active.find_items(locator_sub_title_tools)
            card_description_tools = active.find_items(locator_description_tools)
            print("\n" + card_titles_tools.text + "\n" + card_sub_title_tools.text + "\n" + card_description_tools.text)
            print("-----------------------------------")

        number_of_related_information_card_items = active.related_information_cards_count()

        for y in range(1, number_of_related_information_card_items + 1):
            locator_title_related_information = {"by": By.XPATH,
                                                 "value": "/html/body/section[6]/div/div/div[(" + str(
                                                     y) + ")]/a/div/div[2]/h3"}
            locator_description_related_information = {"by": By.XPATH,
                                                       "value": "/html/body/section[6]/div/div/div[(" + str(
                                                           y) + ")]/a/div/div[2]/p"}

            card_titles_related_information = active.find_items(locator_title_related_information)
            card_description_related_information = active.find_items(locator_description_related_information)
            print("\n" + card_titles_related_information.text + "\n" + card_description_related_information.text)
            print("-----------------------------------")

        active.click_on_view_all_related_information_cta()
        time.sleep(2)
        selected_option = "ACTive Coiled Tubing Services"

        assert (active.selected_option_get_text() == selected_option, "The selected option text is incorrect")
