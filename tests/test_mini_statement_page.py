from pages.mini_statement_page import MiniStatementPage
import pytest

@pytest.mark.usefixtures("login")
class TestMiniStatementPage:
    def test_mini_statement_page_is_shown(self, driver, username_password):
        statement_page = MiniStatementPage(driver)
        statement_page.click_mini_statement_link()
        assert statement_page.is_mini_statement_page(), "Mini statement page is not shown!"

    def test_reset_account_no(self, driver):
        statement_page = MiniStatementPage(driver)
        statement_page.select_account_no()
        statement_page.click_reset_btn()
        assert statement_page.account_no_is_reset(), "Reset Account Number Failed!"