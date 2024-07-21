import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_api.helper import attach_helpers
from test_api.helper.attach_helpers import add_screenshot, add_logs, add_html, add_video, mobile_attach_video
from test_api.helper.get_env_path import get_personal_env_path


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Browser for test',
        choices=['firefox', 'chrome'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        help='Version of browser',
        choices=['126.0', '125.0'],
        default='126.0'
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")

@pytest.fixture()
def api_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
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


