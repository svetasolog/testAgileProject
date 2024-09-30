from pages.base_page import BasePage
from pages.mini_statement_page_locators import MiniStatementPageLocators
from resources.constants import MAX_WAIT_INTERVAL, MINI_STATEMENT_TEXT, ACCOUNT_NO_SELECT_INDEX, ACCOUNT_NO_RESET_VALUE
from selenium.webdriver.support.select import Select

class MiniStatementPage(BasePage):

    def click_mini_statement_link(self):
        self.find_element(MiniStatementPageLocators.MINI_STATEMENT_LINK).click()

    def is_mini_statement_page(self):
        page_header_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, MiniStatementPageLocators.MINI_STATEMENT_PAGE_LBL).text
        if page_header_text == MINI_STATEMENT_TEXT:
            return True
        else:
            return False

    def select_account_no(self):
        account_no_list = Select(self.find_element(MiniStatementPageLocators.ACCOUNT_NO_LIST))
        account_no_list.select_by_index(ACCOUNT_NO_SELECT_INDEX)

    def click_reset_btn(self):
        self.find_element(MiniStatementPageLocators.RESET_BTN).click()

    def account_no_is_reset(self):
        account_no_list = Select(self.find_element(MiniStatementPageLocators.ACCOUNT_NO_LIST))
        selected_value = account_no_list.first_selected_option.text
        if selected_value == ACCOUNT_NO_RESET_VALUE:
            return True
        else:
            return False