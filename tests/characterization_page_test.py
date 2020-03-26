import time

import pytest

from pages import characterization_page
from tests.config import all_characterization_link


class TestCharacterizationOption():
    @pytest.fixture
    def characterization(self, driver):
        return characterization_page.CharacterizatonPage(driver)

    def test_characterization_main_nav(self, driver, characterization):
        hero_text_h1_text = "Reservoir Characterization"
        hero_text_h2_text = "Advance your understanding to optimize reservoir performance"
        characterization.navigate_to_slb()
        time.sleep(3)

        if characterization.in_menu_nav_bar_is_displayed():
            characterization.click_on_characterization_main_nav()
            time.sleep(3)
            characterization.click_on_all_characterization_sub_nav()
            time.sleep(3)
            assert (all_characterization_link == characterization._get_current_url(), "The link has been changed")

            if characterization.hero_section_is_displayed():
                assert (hero_text_h1_text == characterization.hero_text_h1_get_text(), "The H1 text has been changed")
                assert (hero_text_h2_text == characterization.hero_text_h2_get_text(), "The H2 text has been changed")
            else:
                print("Hero section is not displayed")

            if characterization.sticky_banner_is_displayed():
                assert (characterization.contact_us_is_displayed(), "Contact Us is not displayed")
                assert (characterization.related_documents_is_displayed(), "Related Documents is not displayed")
            else:
                print("Sticky banner is not displayed")
        else:
            print("The In Menu Nav Bar is not displayed")
