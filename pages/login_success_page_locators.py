from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL

#index page
class LoginSuccessPageLocators(BasePage):

    LOGIN_SUCCESSFUL_LBL = (By.XPATH, "//ul[@class='menusubnav']/li[3]")


