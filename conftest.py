# в требованиях к задаче написано, что достаточно работы с chrome, поэтому часть про работу с FF удалена

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    lang = Options()
    lang.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=lang)
    yield browser
    print("\nquit browser..")
    browser.quit()