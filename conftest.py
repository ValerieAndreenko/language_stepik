import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    #                  help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope='session')
def r_browser(request):
    # browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    try:
        print("\nOpening browser...")
        r_browser = webdriver.Chrome()        
        yield r_browser
    
    # options_firefox = OptionsFirefox()
    # options_firefox.set_preference("intl.accept_languages", user_language)

    # r_browser = None
    # if browser_name == "chrome":
    #     print("\nstart chrome browser for test..")
    #     r_browser = webdriver.Chrome(options=options)
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     r_browser = webdriver.Firefox(options=options_firefox)
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    finally:
        print("\nClosing browser...")
        r_browser.quit()