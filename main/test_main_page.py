import pytest

from main.pages.main_page import MainPage
from main.pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser, getting_language):
    link = f"http://selenium1py.pythonanywhere.com/{getting_language}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()

    login_page = LoginPage(page.browser, browser.current_url)#"http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    login_page.should_be_login_page()


@pytest.mark.parametrize("number", [True, False])
def test_1(pytestconfig, number):
    assert number,  pytestconfig.getoption('language')
