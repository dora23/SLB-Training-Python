import time

import pytest

from pages import contact_us


class TestContactUsPage():
    @pytest.fixture
    def contact(self, driver):
        return contact_us.ContactUs(driver)

    def test_contact_us(self, driver, contact):
        contact.navigate_to_slb()
        time.sleep(2)
        contact_us_link = "https://connect.slb.com/connect-with-us.aspx"
        contact.click_on_contact_us()
        time.sleep(2)

        assert (contact_us_link == contact.get_current_url(), "The link has been changed")

        contact.click_on_drop_down_menu()
        time.sleep(1)
        contact.click_on_drop_down_menu_other()
        time.sleep(2)
        contact.fill_in_contact_form("Andrei", "Test", "mailtest@yahoo.com", "Albania", "123434562", "Usource", "Engineer",
                                     "Cementing", "Test")
        time.sleep(6)
