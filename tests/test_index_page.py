from pages.index_page import IndexPage
from resources.constants import TEST_SITE_URL

class TestIndexPage:

    def test_reset_username_and_password(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_type_user_name_and_password(username_password)
        index_page.click_reset_btn()
        assert index_page.username_and_password_are_reset(), "Reset username and password Failed!"