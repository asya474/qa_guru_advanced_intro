import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_api.helper.attach_helpers import add_screenshot, add_logs, add_html, add_video, mobile_attach_video


@pytest.fixture()
def api_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()
