import time

import pytest

from pages import navigation_bar


class TestNavigationBar():
    @pytest.fixture
    def navigation(self, driver):
        return navigation_bar.NavigationBar(driver)

    def test_navigation_bar(self, driver, navigation):
        navigation.navigate_to_slb()
        time.sleep(2)

        if navigation.navigation_bar_is_displayed():
            assert navigation.characterization_is_displayed()
            assert navigation.drilling_is_displayed()
            assert navigation.completions_is_displayed()
            assert navigation.production_is_displayed()
            assert navigation.intervention_is_displayed()
            assert navigation.insights_is_displayed()
            assert navigation.resource_library_is_displayed()
            assert navigation.locations_is_displayed()
            assert navigation.software_is_displayed()
            print("All the elements are displayed")

        else:
            print("The Navigation Section is not displayed")
