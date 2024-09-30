from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOG_OUT_TEXT


class LoginSuccessPage(BasePage):

    def is_login_success(self):
        login_success_label = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGIN_SUCCESSFUL_LBL).text
        if login_success_label == LOG_OUT_TEXT:
            return True
        else:
            return False


