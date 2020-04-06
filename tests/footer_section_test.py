import time

import pytest
from selenium.webdriver.common.by import By

from pages import footer_section


class TestSFooterSection():
    @pytest.fixture
    def footer(self, driver):
        return footer_section.FooterSection(driver)

    def test_footer_section(self, driver, footer):
        footer.navigate_to_slb()
        time.sleep(3)
        footer.scroll_to_footer_section()

        number_of_footer_links = footer.footer_items_count()

        for x in range(1, number_of_footer_links + 1):
            print("--------------------------------------")
            locator = {"by": By.CSS_SELECTOR,
                       "value": "#footer > div.toppart.row.small-collapse.large-uncollapse.accordion > div:nth-child(" + str(
                           x) + ")"}
            footer_links_title = footer.find_items(locator)
            print("\n" + footer_links_title.text)

    def test_footer_links(self, driver, footer):
        footer.navigate_to_slb()
        time.sleep(3)
        footer.scroll_to_footer_section()

        if footer.logo_footer_is_displayed():
            print(footer.privacy_link_get_text())
            print(footer.terms_link_get_text())
            print(footer.sitemap_link_get_text())
            print(footer.locations_link_get_text())
            print(footer.copyright_logo_get_text())
            print(footer.slb_shares_get_text())

        else:
            print("The logo is not displayed")

        number_of_social_icons_links = footer.social_items_count()

        for x in range(1, number_of_social_icons_links + 1):
            print("--------------------------------------")
            locator_social_media = {"by": By.CSS_SELECTOR,
                       "value": "#footer > div.botpart > div > div.botpart__social > div > a:nth-child(" + str(
                           x) + ")"}
            social_media_title = footer.find_items(locator_social_media)
            print("\n" + social_media_title.get_attribute("title"))