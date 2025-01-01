import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help="Choose browser: Chrome or Firefox")

    parser.addoption("--language", action="store", default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browse for test...")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()
