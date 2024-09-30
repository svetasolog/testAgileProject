from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MiniStatementPageLocators(BasePage):

    MINI_STATEMENT_LINK = (By.XPATH, "//ul[@class='menusubnav']/li[2]")
    MINI_STATEMENT_PAGE_LBL = (By.XPATH, "//*[@class='heading3']")
    ACCOUNT_NO_LIST = (By.NAME, "accountno")
    RESET_BTN = (By.NAME, "res")