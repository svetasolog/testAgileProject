from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOGIN_BTN_TEXT


class IndexPage(BasePage):

    def wait_and_type_user_name_and_password(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.USER_ID_TXTBX).send_keys(
            usr_and_pw[0])
        self.find_element(IndexPageLocators.PASSWORD_TXTBX).send_keys(
            usr_and_pw[1])

    def click_reset_btn(self):
        self.find_element(IndexPageLocators.RESET_BUTTON).click()

    def username_and_password_are_reset(self):
        username_txtbx_text = self.find_element(IndexPageLocators.USER_ID_TXTBX).text
        password_txtbx_text = self.find_element(IndexPageLocators.PASSWORD_TXTBX).text
        if username_txtbx_text == '' and password_txtbx_text == '':
            return True
        else:
            return False
    def click_submit_btn(self):
        self.find_element(IndexPageLocators.LOGIN_SUBMIT_BUTTON).click()

    def is_logged_out(self):
        login_btn_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.LOGIN_SUBMIT_BUTTON).get_attribute('value')
        if login_btn_text == LOGIN_BTN_TEXT:
            return True
        else:
            return False



