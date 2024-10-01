from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOG_OUT_TEXT, LOGOUT_ALERT_MESSAGE


class LoginSuccessPage(BasePage):

    def is_login_success(self):
        login_success_label = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginSuccessPageLocators.LOGOUT_LINK).text
        if login_success_label == LOG_OUT_TEXT:
            return True
        else:
            return False

    def click_logout_link(self):
        self.find_element(LoginSuccessPageLocators.LOGOUT_LINK).click()

    def alert_msg_is_shown(self):
        alert_msg = self.switch_to_alert()
        if alert_msg.text == LOGOUT_ALERT_MESSAGE:
            alert_msg.accept()
            return True
        else:
            return False
