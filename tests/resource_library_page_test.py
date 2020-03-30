import time

import pytest

from pages import resource_library_page


class TestResourceLibraryPage():
    @pytest.fixture
    def filter(self, driver):
        return resource_library_page.ResourceLibraryPage(driver)

    def test_filter_option(self, driver, filter):
        filter.navigate_to_slb()
        time.sleep(2)

        # Topic Filter

        filter.click_on_topic_menu()
        time.sleep(1)
        topic = "ADIPEC"
        filter.select_topic_option(topic)
        time.sleep(1)

        assert (topic == filter.topic_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)
        filter.click_on_topic_menu()

        # Section Filter

        filter.click_on_section_menu()
        time.sleep(1)
        section = "Adaptive Cement Systems"
        filter.select_section_option(section)

        time.sleep(1)
        assert (section == filter.section_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)
        filter.click_on_section_menu()

        # Product Name Filter

        filter.click_on_product_name_menu()
        time.sleep(1)
        filter.click_on_show_more_products()
        product_name = "2M"
        filter.select_product_name_option(product_name)

        time.sleep(1)
        assert (product_name == filter.product_name_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)
        filter.click_on_product_name_menu()

        # Resource Type Filter

        filter.click_on_resource_type_menu()
        time.sleep(1)
        resource_type = "Book"
        filter.select_resource_type_option(resource_type)

        time.sleep(1)
        assert (resource_type == filter.resource_type_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)
        filter.click_on_resource_type_menu()

        # Country Filter

        filter.click_on_country_menu()
        time.sleep(1)
        country = "Australia"
        filter.select_country_option(country)

        time.sleep(1)
        assert (country == filter.country_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)
        filter.click_on_country_menu()

        # Region Filter

        filter.click_on_region_menu()
        time.sleep(1)
        region = "Campos Basin"
        filter.select_region_option(region)

        time.sleep(1)
        assert (region == filter.region_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        time.sleep(1)

        # State Filter

        filter.click_on_state_menu()
        time.sleep(1)
        state = "California"
        filter.select_state_option(state)

        time.sleep(1)
        assert (state == filter.state_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        filter.click_on_state_menu()

        # Year Filter

        filter.click_on_year_menu()
        time.sleep(1)
        year = "2018"
        filter.select_year_option(year)

        time.sleep(1)
        assert (year == filter.year_selected_option_get_text(), "The text is incorrect")
        time.sleep(1)
        filter.click_on_clear_all_button()
        filter.click_on_year_menu()

    def test_all_filters_option(self, driver, filter):
        time.sleep(1)
        topic = "ADIPEC"
        section = "Reservoir Testing"
        product_name = "Concert"
        resource_type = "Industry Article"
        year = "2018"

        filter.navigate_to_slb()
        time.sleep(1)

        filter.click_on_topic_menu()
        filter.select_topic_option(topic)
        time.sleep(1)

        filter.click_on_section_menu()
        filter.select_section_option(section)
        time.sleep(1)

        filter.click_on_product_name_menu()
        filter.select_product_name_option(product_name)
        time.sleep(1)

        filter.click_on_resource_type_menu()
        filter.select_resource_type_option(resource_type)
        time.sleep(1)

        filter.click_on_year_menu()
        filter.select_year_option(year)
        time.sleep(1)

        assert (topic == filter.topic_selected_option_get_text(), "The text is incorrect")
        assert (section == filter.section_selected_option_get_text(), "The text is incorrect")
        assert (product_name == filter.product_name_selected_option_get_text(), "The text is incorrect")
        assert (resource_type == filter.resource_type_selected_option_get_text(), "The text is incorrect")
        assert (year == filter.year_selected_option_get_text(), "The text is incorrect")
