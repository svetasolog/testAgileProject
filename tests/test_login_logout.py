from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from pages.index_page import IndexPage
import pytest

@pytest.mark.usefixtures("login")
class TestLogin:

    def test_login(self, driver):
        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.is_login_success(), "Login Failed!"

    def test_logout(self, driver):
        login_success_page = LoginSuccessPage(driver)
        login_success_page.click_logout_link()
        assert login_success_page.alert_msg_is_shown(), "Logout alert message Failed!"
        index_page = IndexPage(driver)
        assert index_page.is_logged_out(), "Log out Failed!"
