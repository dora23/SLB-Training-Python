import time

import pytest

from pages import search_function


class TestSearchFunctionality():
    @pytest.fixture
    def search(self, driver):
        return search_function.SearchFunctionality(driver)

    def test_search_option(self, driver, search):
        search.navigate_to_slb()
        time.sleep(2)

        search.fill_in_searched_word("test")
        time.sleep(3)
        assert (search.searched_word_get_text() == "test")
        time.sleep(1)

        # Product Filter

        product = "Saturn"
        search.select_product_option(product)
        time.sleep(3)

        assert (product == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_product_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)

        # Content Type Filter

        content_type = "Topic Page"
        search.select_content_type_option(content_type)
        time.sleep(2)

        assert (content_type == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_content_type_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)

        # Country Filter

        country = "Brazil"
        search.select_country_option(country)
        time.sleep(2)

        assert (country == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_country_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)

        # Challenge Filter

        challenge = "Carbonates"
        search.select_challenge_option(challenge)
        time.sleep(2)

        assert (challenge == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_challenge_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)

        # Topic Filter

        topic = "Completions"
        search.select_topic_option(topic)
        time.sleep(2)

        assert (topic == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_topic_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)

        # Year Filter

        year = "2016"
        search.select_year_option(year)
        time.sleep(2)

        assert (year == search.selected_option_get_text(), "The text is incorrect")
        assert (search.results_nr_get_text() == search.nr_of_results_displayed_year_get_text(),
                "Results number doesn't match")

        search.click_on_clear_all_button()
        time.sleep(2)