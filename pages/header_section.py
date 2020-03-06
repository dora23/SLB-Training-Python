from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    header_section = {"by": By.CLASS_NAME, "value": 'mainbar__container'}