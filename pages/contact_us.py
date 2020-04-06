from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.config import baseurl


class ContactUs(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    contact_us_link = {"by": By.CSS_SELECTOR,
                       "value": 'body > header > div:nth-child(1) > div > div.mainbar > div.mainbar__actions > a.mainbar__actions__btn.btn--order'}

    drop_down_menu = {"by": By.CSS_SELECTOR,
                      "value": '#form_339E8AA1892F45179D12B3A4C77B8CC4_field_FFA7ED912199487AABB044B458C079BE'}

    drop_down_menu_other = {"by": By.CSS_SELECTOR,
                            "value": '#form_339E8AA1892F45179D12B3A4C77B8CC4_field_FFA7ED912199487AABB044B458C079BE > option:nth-child(14)'}

    first_name_text_area = {"by": By.CSS_SELECTOR,
                            "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_F37A0F2CDF26488EA6A0FF4510271C5C"]'}

    last_name_text_area = {"by": By.CSS_SELECTOR,
                           "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_CB2CEB86774D4604936361B8821720BD"]'}

    e_mail_text_area = {"by": By.CSS_SELECTOR,
                        "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_DAF4F49EB212484D8E7B27D6E5BB5BEB"]'}

    phone_number_text_area = {"by": By.CSS_SELECTOR,
                              "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_299AB8C72795465D9E67E6C17E4434E6"]'}

    company_text_area = {"by": By.CSS_SELECTOR,
                         "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_83A0C29886074605A453D36607D09DB9"]'}

    job_title_text_area = {"by": By.CSS_SELECTOR,
                           "value": 'input[id="form_E02383204E804037BBC8616AD3BA6093_field_0DA8E01C4A6349E88F6827CD9F2A2F9F"]'}

    comments_text_area = {"by": By.CSS_SELECTOR,
                          "value": 'textarea[id="form_E02383204E804037BBC8616AD3BA6093_field_EB49297DDC804CC18F7E1530ACBF27E8"]'}

    region_dropdown_option = {"by": By.CSS_SELECTOR,
                              "value": 'select[id="form_E02383204E804037BBC8616AD3BA6093_field_A282975822DB4F52A2E33FF1D3993B4F"]'}

    interested_in_dropdown_option = {"by": By.CSS_SELECTOR,
                                     "value": 'select[id="form_E02383204E804037BBC8616AD3BA6093_field_CB51E96D8DA14DC0B746CCA4E1D9B1A4"]'}

    def navigate_to_slb(self):
        self._visit(baseurl)

    def click_on_contact_us(self):
        self._click(self.contact_us_link)

    def click_on_drop_down_menu(self):
        self._click(self.drop_down_menu)

    def click_on_drop_down_menu_other(self):
        self._click(self.drop_down_menu_other)

    def get_current_url(self):
        return self.driver.current_url

    def fill_in_contact_form(self, first_name, last_name, e_mail, region, phone_number, company, job_title,
                             interested_in, comments):
        self._click(self.first_name_text_area)
        self._type(self.first_name_text_area, first_name)
        self._click(self.last_name_text_area)
        self._type(self.last_name_text_area, last_name)
        self._click(self.e_mail_text_area)
        self._type(self.e_mail_text_area, e_mail)
        self._click(self.region_dropdown_option)
        self._select_dropdown_option(self.region_dropdown_option, region)
        self._click(self.phone_number_text_area)
        self._type(self.phone_number_text_area, phone_number)
        self._click(self.company_text_area)
        self._type(self.company_text_area, company)
        self._click(self.job_title_text_area)
        self._click(self.interested_in_dropdown_option)
        self._select_dropdown_option(self.interested_in_dropdown_option, interested_in)
        self._type(self.job_title_text_area, job_title)
        self._click(self.comments_text_area)
        self._type(self.comments_text_area, comments)
