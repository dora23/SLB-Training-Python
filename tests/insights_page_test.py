import time

import pytest
from selenium.webdriver.common.by import By

from pages import insights_page
from tests.config import insightsurl


class TestInsightsPage():
    @pytest.fixture
    def insights(self, driver):
        return insights_page.InsightsPage(driver)

    def test_insights_page(self, driver, insights):
        insights.navigate_to_slb()
        time.sleep(2)
        insights.click_on_insights_menu_option()
        time.sleep(1)
        current_link = "https://www.slb.com/resource-library/interview/slb/interview---lees-rodionov-at-bloomberg"

        if insightsurl == insights.return_current_url():
            print("The link is correct")
        else:
            print("The link has been changed")

        if insights.hero_section_is_displayed():
            print(insights.hero_title_get_text())
            print(insights.hero_subtitle_get_text())
        else:
            print("The title or subtitle is not displayed")

        if insights.hero_cta_button_is_displayed():
            insights.click_on_hero_cta_button()
            time.sleep(3)
            assert (current_link == insights.return_current_url(), "The link has been changed")
            time.sleep(1)

        # Card Items Count

    def test_cards(self, driver, insights):
        insights.navigate_to_insightsurl()
        time.sleep(2)

        number_of_card_items = insights.article_cards_count()

        if 12 == number_of_card_items:
            print("There are 12 cards listed")
        else:
            print("The number is incorrect")

        assert (insights.load_more_button_is_displayed(), "The Load More button is not displayed")
        insights.click_on_load_more_button()
        time.sleep(3)
        updated_card_items = insights.article_cards_count()
        print(updated_card_items)

    def test_print_card_title_and_description(self, driver, insights):
        insights.navigate_to_insightsurl()
        time.sleep(2)

        number_of_card_items = insights.article_cards_count()
        for x in range(1, number_of_card_items + 1):
            locator_title = {"by": By.CSS_SELECTOR,
                             "value": "div.tiles__wrapper > div.tiles > div:nth-child(" + str(
                                 x) + ") > div > div > a"}
            locator_description = {"by": By.CSS_SELECTOR,
                                   "value": "div.tiles__wrapper > div.tiles > div:nth-child(" + str(
                                       x) + ") > div > div.tile__desc"}

            card_titles = insights.find_items(locator_title)
            card_description = insights.find_items(locator_description)
            print("\n" + card_titles.text + "\n" + card_description.text)
            print("-----------------------------------")

    def test_browse_by_filter(self, driver, insights):
        insights.navigate_to_insightsurl()
        time.sleep(2)

        insights.click_on_well_phase_option()
        time.sleep(2)
        well_phase = "Corporate"
        insights.select_well_phase_option(well_phase)
        time.sleep(2)

        if well_phase == insights.well_phase_selected_option_get_text():
            print("The " + insights.well_phase_selected_option_get_text() + " option has been selected correctly")

        insights.click_on_clear_all_button()
        time.sleep(3)

        insights.click_on_trending_topic_option()
        time.sleep(1)
        trending_option = "Automation"
        insights.select_trending_topic_option(trending_option)
        time.sleep(2)

        if trending_option == insights.trending_topic_selected_option_get_text():
            print("The " + insights.trending_topic_selected_option_get_text() + " option has been selected correctly")

        insights.click_on_clear_all_button()
        time.sleep(3)

        insights.click_on_type_option()
        time.sleep(1)
        type_option = "Video"
        insights.select_type_option_option(type_option)
        time.sleep(2)

        if type_option == insights.type_option_selected_option_get_text():
            print("The " + insights.type_option_selected_option_get_text() + " option has been selected correctly")

        insights.click_on_clear_all_button()
        time.sleep(3)
