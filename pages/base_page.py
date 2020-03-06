from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _scroll_to_element(self, locator):
        element = self._find(locator)
        return ActionChains(self.driver).move_to_element(element).perform()

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_current_url(self):
        return self.driver.current_url

    def _hover(self, locator):
        return ActionChains(self.driver).move_to_element(locator).perform()

    def _select_dropdown_option(self, locator, option_text):
        dropdown = Select(self._find(locator))
        for option in dropdown.options:
            dropdown.select_by_visible_text(option_text)
            if option.text == option_text:
                option.click()
                break

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def _wait_for_is_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True

    def _press_enter_button(self, locator):
        element = self._find(locator)
        element.send_keys(Keys.ENTER)

    def _get_attribute(self, locator, attribute):
        element = self._find(locator)
        attr_value = element.get_attribute(attribute)
        return attr_value
