from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser, getting_language):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.check_item_in_basket()
    print("Product has been added to basket")
