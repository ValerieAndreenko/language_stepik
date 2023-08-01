import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru' or '--language=es' or '--language=fr'")


@pytest.fixture(scope='session')
def r_browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    try:
        print("\nOpening browser...")
        r_browser = webdriver.Chrome(options=options)        
        yield r_browser
    finally:
        print("\nClosing browser...")
        r_browser.quit()