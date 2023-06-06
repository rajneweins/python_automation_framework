from selenium.webdriver.common.by import By


class LoginLocators:
    TITLE = (By.XPATH, "//div[contains(text(),'Helios')]")
    # USERNAME_INPUT = (By.ID, "username")
    # PASSWORD_INPUT = (By.ID, "password")
    # LOGIN_BUTTON = (By.ID, "login-button")
    # LOGOUT_BUTTON = (By.ID, "logout-button")
    # WELCOME_MESSAGE = (By.XPATH, "//div[@class='welcome-message']")
    # ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message']")
    USERNAME_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    