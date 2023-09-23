import pytest

from main.pages.basket_page import BasketPage
from main.pages.main_page import MainPage
from main.pages.login_page import LoginPage
from main.pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser, getting_language):
    link = f"http://selenium1py.pythonanywhere.com/{getting_language}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()

    login_page = LoginPage(page.browser, browser.current_url)#"http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    login_page.should_be_login_page(language=getting_language)


@pytest.mark.parametrize("number", [True, False])
@pytest.mark.skip
def test_1(pytestconfig, number):
    assert number,  pytestconfig.getoption('language')


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, getting_language):
    link = f"http://selenium1py.pythonanywhere.com/{getting_language}/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    assert len(basket_page.get_basket_items()) == 0, "Wrong items count in basket"
    basket_page.should_be_empty_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, getting_language):
    link = f"http://selenium1py.pythonanywhere.com/{getting_language}/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    # page.add_to_basket() # negative case
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    assert len(basket_page.get_basket_items()) == 0, "Wrong items count in basket"
    basket_page.should_be_empty_basket()
