from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginSuccessPageLocators(BasePage):

    LOGOUT_LINK = (By.XPATH, "//ul[@class='menusubnav']/li[3]")


