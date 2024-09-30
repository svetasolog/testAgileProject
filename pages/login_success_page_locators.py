from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginSuccessPageLocators(BasePage):

    LOGIN_SUCCESSFUL_LBL = (By.XPATH, "//ul[@class='menusubnav']/li[3]")


