import pytest as pytest
from selenium import webdriver
from pages.index_page import IndexPage
from resources.constants import TEST_SITE_URL


@pytest.fixture(scope="module")
def username_password():
    user_name = "1303"
    password = "Guru99"
    return [user_name, password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture(scope="module")
def login(driver, username_password):
    index_page = IndexPage(driver)
    index_page.navigate_to(TEST_SITE_URL)
    index_page.wait_and_type_user_name_and_password(username_password)
    index_page.click_submit_btn()