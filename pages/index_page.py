from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, TEST_SITE_URL, SIGN_ON_BTN_TEXT


#index page
class IndexPage(BasePage):

    def wait_and_click_register_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()
        # test comment on index_page.py

    def login_using_username_password(self,user_name, password):
        self.navigate_to(TEST_SITE_URL)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.USER_NAME_TXTBX).send_keys(user_name)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.PASSWORD_TXTBX).send_keys(password)
        self.find_element(IndexPageLocators.LOGIN_SUBMIT_BUTTON).click()

    def is_logged_out(self):
        sign_on_btn_text =self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.SIGN_ON_BUTTON).text
        if(sign_on_btn_text==SIGN_ON_BTN_TEXT):
            return True
        else:
            return False



