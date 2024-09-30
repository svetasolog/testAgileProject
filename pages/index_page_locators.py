from selenium.webdriver.common.by import By

# index locators
class IndexPageLocators:

    REGISTER_LINK = (By.XPATH, "//a[text()='REGISTER']")
    OK_BUTTON = (By.NAME, "btn_ok")
    USER_NAME_TXTBX = (By.NAME, "userName")
    PASSWORD_TXTBX = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "submit")
    SIGN_ON_BUTTON = (By.XPATH,"//td[@width='67']/a")
