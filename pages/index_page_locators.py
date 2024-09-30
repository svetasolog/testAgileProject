from selenium.webdriver.common.by import By

# index locators
class IndexPageLocators:

    USER_ID_TXTBX = (By.NAME, "uid")
    PASSWORD_TXTBX = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "btnLogin")
    RESET_BUTTON = (By.NAME,"btnReset")
