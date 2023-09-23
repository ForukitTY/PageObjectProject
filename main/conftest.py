import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', help='language (ru, en-gb)', default='ru')


@pytest.fixture
def getting_language(request):
    lang = request.config.getoption("--language")
    return lang


@pytest.fixture
def browser(getting_language):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('prefs', {'intl.accept_languages': getting_language})

    wb = webdriver.Chrome(options=options)
    # wb.implicitly_wait(3)
    yield wb
    time.sleep(3)
    wb.quit()
