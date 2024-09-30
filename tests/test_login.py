# from test_utils import *
from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from pages.mini_statement_page import MiniStatementPage
from resources.constants import TEST_SITE_URL


class TestProject:

    def test_reset_username_and_password(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_type_user_name_and_password(username_password)
        index_page.click_reset_btn()
        assert index_page.username_and_password_are_reset(), "Reset username and password Failed!"

    def test_login(self, driver, username_password):
        index_page = IndexPage(driver)
        # index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_type_user_name_and_password(username_password)
        index_page.click_submit_btn()

        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.is_login_success(), "Login Failed!"

    def test_mini_statement_page_is_shown(self, driver):
        statement_page = MiniStatementPage(driver)
        statement_page.click_mini_statement_link()
        assert statement_page.is_mini_statement_page(), "Mini statement page is not shown!"

    def test_reset_account_no(self, driver):
        statement_page = MiniStatementPage(driver)
        statement_page.select_account_no()
        statement_page.click_reset_btn()
        assert statement_page.account_no_is_reset(), "Reset Account Number Failed!"