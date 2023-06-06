import pytest
from selenium import webdriver
from browserstack.local import Local
# from seleniumrequests import Chrome, Firefox
# from browserstack import BrowserStack
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
import os
load_dotenv()


@pytest.fixture(scope="session")
def browser(request):
    browser_type = os.getenv("BROWSER_TYPE", "chrome")
    browser_version = os.getenv("BROWSER_VERSION", "latest")

    desired_caps = {
        "os": "Windows",
        "os_version": "10",
        "name": "Helios",
    }

    if browser_type.lower() == "chrome":
        desired_caps["browser"] = "Chrome"
        desired_caps["browser_version"] = browser_version
        desired_caps["acceptInsecureCerts"] = True
        desired_caps["goog:chromeOptions"] = {
            "args": ["--disable-infobars", "--disable-extensions"]
        }
        driver = webdriver.Chrome
    elif browser_type.lower() == "firefox":
        desired_caps["browser"] = "Firefox"
        desired_caps["browser_version"] = browser_version
        desired_caps["acceptInsecureCerts"] = True
        driver = webdriver.Firefox
    else:
        raise ValueError(f"Invalid browser type: {browser_type}")

    bs_local = None
    if "BROWSERSTACK_USERNAME" in os.environ:
        bs_local = Local()
        bs_local.start(key=os.environ["BROWSERSTACK_ACCESS_KEY"])
        desired_caps["browserstack.local"] = True

    browser = driver(desired_capabilities=desired_caps)

    def close_browser():
        browser.quit()
        if bs_local is not None:
            bs_local.stop()

    request.addfinalizer(close_browser)
    return browser
