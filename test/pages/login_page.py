from test.locators.login_locators import LoginLocators
from test.locators.homepage_locators import HomePageLocators
from resources.config import Config
from test.testdata.login_test_Data import LoginTestData as ltd



class LoginPage:
    def __init__(self):
        self.browser = None
    
    def set_browser(self, browser):
        self.browser = browser
    
    def go_to_login_page(self):
        self.browser.get(Config.LOGIN_URL)
    
    def enter_username(self, username):
        username_input = self.browser.find_element(*LoginLocators.USERNAME_INPUT)
        username_input.clear()
        # username_input.send_keys(username)
        username_input.send_keys(ltd.VALID_USERNAME)
    
    def click_login_button(self):
        login_button = self.browser.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()
    
    def enter_password(self, password):
        password_input = self.browser.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(ltd.VALID_PASSWORD)
    
    def enter_credentials(self, username, password):
        username_input = self.browser.find_element(*LoginLocators.USERNAME_INPUT)
        password_input = self.browser.find_element(*LoginLocators.PASSWORD_INPUT)
        
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
    
    # def click_login_button(self):
    #     login_button = self.browser.find_element(*LoginLocators.LOGIN_BUTTON)
    #     login_button.click()
    
    # def click_logout_button(self):
    #     logout_button = self.browser.find_element(*LoginLocators.LOGOUT_BUTTON)
    #     logout_button.click()
    
    def is_login_successful(self):
        welcome_message = self.browser.find_element(*LoginLocators.TITLE)
        return welcome_message.text
    
    # def is_logout_successful(self):
    #     login_button = self.browser.find_element(*LoginLocators.LOGIN_BUTTON)
    #     return login_button.is_displayed()
    
    # def is_error_message_displayed(self):
    #     error_message = self.browser.find_element(*LoginLocators.ERROR_MESSAGE)
    #     return error_message.is_displayed()
    
    # def get_error_message(self):
    #     error_message = self.browser.find_element(*LoginLocators.ERROR_MESSAGE)
    #     return error_message.text
    
    def is_genesys_mode_enabled(self):
        button = self.browser.find_element(*HomePageLocators.BUTTON_GENESYS_MODE)
        return button.get_attribute("aria-pressed")
        
