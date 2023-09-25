import pytest

from main.pages.basket_page import BasketPage
from main.pages.locators import ProductPageLocators
from main.pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(link, browser, getting_language):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.check_item_in_basket()
    print("Product has been added to basket")


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()

    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    assert page.url == login_url, "Opened page has no login url"


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, getting_language):
    link = f"http://selenium1py.pythonanywhere.com/{getting_language}/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    # page.add_to_basket() # negative case
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    assert len(basket_page.get_basket_items()) == 0, "Wrong items count in basket"
    basket_page.should_be_empty_basket()
