from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, SIGN_ON_BTN_TEXT


class IndexPage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.USER_ID_TXTBX).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(IndexPageLocators.PASSWORD_TXTBX).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(IndexPageLocators.LOGIN_SUBMIT_BUTTON).click()

    def is_logged_out(self):
        sign_on_btn_text =self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.SIGN_ON_BUTTON).text
        if(sign_on_btn_text==SIGN_ON_BTN_TEXT):
            return True
        else:
            return False



