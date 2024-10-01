from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    def test_login(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_type_user_name_and_password(username_password)
        index_page.click_submit_btn()

        login_success_page = LoginSuccessPage(driver)
        assert login_success_page.is_login_success(), "Login Failed!"

    # def test_logout(self, driver):
