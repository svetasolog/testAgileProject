from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL, TEST_SITE_URL, LOGIN_SUCCESS_MESSAGE_TEXT, SIGN_OFF_BTN_TEXT


#index page
class LoginSuccessPage(BasePage):

    def is_login_success(self):
        login_success_label = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGIN_SUCCESSFUL_LBL).text
        if(login_success_label==LOGIN_SUCCESS_MESSAGE_TEXT):
            return True
        else:
            return False

    def log_out_if_logged_in(self):
        logout_btn_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginSuccessPageLocators.LOGOUT_BTN).text
        if(logout_btn_text == SIGN_OFF_BTN_TEXT):
            self.find_element(LoginSuccessPageLocators.LOGOUT_BTN).click()
            self.driver.refresh()
            self.find_element(LoginSuccessPageLocators.LOGOUT_BTN).click()
            return True
        else:
            return False









