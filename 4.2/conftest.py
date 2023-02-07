import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', help='Do foo')
#
#
# @pytest.fixture
# def language(zxc):
#     lang = zxc.getoption("--language")
#     return lang


@pytest.fixture
def browser():

    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})

    wb = webdriver.Chrome()

    yield wb
    time.sleep(5)
    wb.quit()
