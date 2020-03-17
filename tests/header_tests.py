import time

import pytest

from pages import header_section
from tests.config import who_we_are_url, newsroom_url, careers_url, investors_url, global_stewardship_url


class TestsHeader():
    @pytest.fixture
    def header(self, driver):
        return header_section.Header(driver)

    def test_header_section_elements(self, driver, header):
        header.navigate_to_slb()
        time.sleep(2)

        if header.header_section_is_displayed():
            assert header.slb_logo_is_displayed()
            assert header.who_we_are_is_displayed()
            assert header.newsroom_is_displayed()
            assert header.careers_is_displayed()
            assert header.investor_is_displayed()
            assert header.global_stewardship_is_displayed()
            assert header.search_field_is_displayed()
            assert header.sign_in_button_is_displayed()
            assert header.contact_button_is_displayed()
            print("All the elements are displayed")
        else:
            print("The Header Section is not displayed")

        # def test_who_we_are_navigation(self, driver, header):
        # Who We Are navigation test
        # header.navigate_to_slb()
        # time.sleep(2)
        header.click_on_who_we_are()
        time.sleep(2)
        assert (who_we_are_url == header.get_current_url_link())

        # def test_newsroom_navigation(self, driver, header):
        # Newsroom navigation test
        header.navigate_to_slb()
        time.sleep(2)
        header.click_on_newsroom()
        time.sleep(2)
        assert (newsroom_url == header.get_current_url_link())

    # def test_careers_navigation(self, driver, header):
        # Careers navigation test
        header.navigate_to_slb()
        time.sleep(2)
        header.click_on_careers()
        time.sleep(2)
        assert (careers_url == header.get_current_url_link())

    # def test_investors_navigation(self, driver, header):
        # Investors navigation test
        header.navigate_to_slb()
        time.sleep(2)
        header.click_on_investor()
        time.sleep(2)
        assert (investors_url == header.get_current_url_link())

    # def test_global_stewardship_navigation(self, driver, header):
        # Global Stewardship navigation test
        header.navigate_to_slb()
        time.sleep(2)
        header.click_on_global_stewardship()
        time.sleep(2)
        assert (global_stewardship_url == header.get_current_url_link())

    # def test_search_functionality(self, driver, header):
        # Search Functionality navigation test
        searched_word = "test"
        header.navigate_to_slb()
        time.sleep(2)
        header.click_in_search_field()
        header.search_function(searched_word)
        time.sleep(2)
        header.click_on_search_button()
        time.sleep(2)
        assert ("https://www.slb.com/search#q=" + searched_word + "&t=slbcom" == header.get_current_url_link())
