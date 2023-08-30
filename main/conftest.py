import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', help='Do foo', default='ru')


@pytest.fixture
def getting_language(request):
    lang = request.config.getoption("--language")
    return lang


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    # options.add_experimental_option('prefs', {'intl.accept_languages': getting_language})
    wb = webdriver.Chrome(options=options)
    # wb.implicitly_wait(3)
    yield wb
    wb.quit()
