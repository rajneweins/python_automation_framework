import pytest
from test.pages.login_page import LoginPage
from test.testdata.login_test_Data import LoginTestData as ltd
import time
from test.locators.homepage_locators import HomePageLocators as hpl


@pytest.fixture(scope="class")
def login_page(browser):
    login_page = LoginPage()
    login_page.set_browser(browser)
    return login_page


@pytest.mark.usefixtures("login_page")
class TestLoginPage:
    
    def test_successful_login(self, login_page):
        login_page.go_to_login_page()
        time.sleep(2)
        login_page.enter_username(ltd.VALID_USERNAME)
        login_page.click_login_button()
        time.sleep(10)
        assert login_page.is_login_successful() == ltd.TITLE
    
    def test_genesysMode(self, login_page):
        assert login_page.is_genesys_mode_enabled()
    
    # @pytest.mark.usefixtures("login_invalid")
    # def test_failed_login_invalid_credentials(self, login_page):
    #     login_page.enter_credentials(ltd.INVALID_USERNAME, ltd.INVALID_PASSWORD)
    #     login_page.click_login_button()
    #     assert login_page.is_error_message_displayed()
    
    # def test_failed_login_blank_fields(self, login_page):
    #     login_page.enter_credentials("", "")
    #     login_page.click_login_button()
    #     assert login_page.is_error_message_displayed()
    #     assert login_page.get_error_message() == "Please enter username and password."
    
    # def test_failed_login_locked_account(self, login_page):
    #     login_page.enter_credentials(ltd.INVALID_USERNAME, ltd.INVALID_PASSWORD)
    #     login_page.click_login_button()
    #     assert login_page.is_error_message_displayed()
    #     assert login_page.get_error_message() == "Your account has been locked."
    
    # def test_successful_logout(self, login_page):
    #     login_page.enter_credentials(ltd.VALID_USERNAME, ltd.VALID_PASSWORD)
    #     login_page.click_login_button()
    #     assert login_page.is_login_successful()
    
    #     login_page.click_logout_button()
    #     assert login_page.is_logout_successful()
