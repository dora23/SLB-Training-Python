import time

import pytest
from selenium.webdriver.common.by import By

from pages import audit_to_optimize


class TestAuditPage():
    @pytest.fixture
    def audit(self, driver):
        return audit_to_optimize.AuditPage(driver)

    def test_audit_page(self, driver, audit):
        audit.navigate_to_slb()
        time.sleep(2)

        audit.click_on_prod_cta_option()
        time.sleep(1)
        audit.click_on_audit_cta_option()
        time.sleep(2)

        if audit.hero_section_is_displayed():
            assert (audit.breadcrumbs_is_displayed(), "The breadcrumbs are not displayed")
            assert (audit.contact_us_cta_is_displayed(), "The Contact Us CTA button is not displayed")
            assert (audit.related_documents_cta_is_displayed(), "The Related Documents CTA button is not displayed")
            print(audit.hero_title_get_text())
            print(audit.hero_subtitle_get_text())
            print("-----------------------------------")
        else:
            print("The Hero Section is not displayed")

        if audit.two_col_component_is_displayed():
            assert (audit.two_col_component_text_is_displayed(), "The Two Column text is not displayed")
            assert (audit.two_col_component_image_is_displayed(), "The Two Column image is not displayed")
        else:
            print("The Two Column component is not displayed")

        if audit.hero_promo_is_displayed():
            assert (audit.hero_promo_cta_button_is_displayed(), "The Hero Promo CTA button is not displayed")
        else:
            print("The Hero Promo Section is not displayed")

        if audit.second_two_col_component_is_displayed():
            assert (audit.second_two_col_component_text_is_displayed(), "The text for the Second Col. comp it not displayed")
            assert (audit.second_two_col_component_image_is_displayed(), "The image for the Second Col. comp is not displayed")
        else:
            print("The second Two Column component is not displayed")

        number_of_card_items = audit.related_products_cards_count()

        for x in range(1, number_of_card_items + 1):

            locator_title = {"by": By.CSS_SELECTOR,
                                 "value": "body > section.column-card-list.column-card-list--gray-back > div > div.cards > div:nth-child(" + str(
                                     x) + ") > a > div > div.content > h3"}
            locator_sub_title = {"by": By.CSS_SELECTOR,
                                 "value": "body > section.column-card-list.column-card-list--gray-back > div > div.cards > div:nth-child(" + str(
                                     x) + ") > a > div > div.content > h4"}

            locator_description = {"by": By.CSS_SELECTOR,
                                   "value": "body > section.column-card-list.column-card-list--gray-back > div > div.cards > div:nth-child(" + str(
                                       x) + ") > a > div > div.content > p"}

            card_titles = audit.find_items(locator_title)
            card_sub_title = audit.find_items(locator_sub_title)
            card_description = audit.find_items(locator_description)
            print("\n" + card_titles.text + "\n" + card_sub_title.text + "\n" + card_description.text)
            print("-----------------------------------")

    def test_audit_footer(self, driver, audit):
        audit.navigate_to_slb_audit()
        time.sleep(4)
        audit.scroll_to_related_information_banner()
        time.sleep(2)

        if audit.related_information_banner_is_displayed():
            print("\n" + audit.related_information_title_get_text())
            print("\n" + audit.related_information_description_get_text())
            print("-----------------------------------")
        else:
            print("Related Information banner is not displayed")

        audit_page_title = audit.hero_title_get_text()
        audit.click_on_view_all_cta_button()
        time.sleep(2)

        assert (audit_page_title == audit.selected_option_get_text(), "The selected option is incorrect")
