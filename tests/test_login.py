from pages.login_success_page import LoginSuccessPage
# from test_utils import *
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    # Test Case 1 ( Registering the user)
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    def test_login_as_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.login_using_username_password(username_password[0], username_password[1])
        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.is_login_success(), "Login Failed!"

    def test_logout(self,driver,username_password):
        index_page = IndexPage(driver)
        index_page.login_using_username_password(username_password[0], username_password[1])
        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.log_out_if_logged_in(), "User is not logged in to the system!"
        assert index_page.is_logged_out(),"Unable to sign out!"


