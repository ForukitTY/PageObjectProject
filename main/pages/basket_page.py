from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from main.pages.base_page import BasePage
from main.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """
        Проверяет на существование прямого потомка <p> у #content_inner
        """
        try:
            self.browser.find_element(*BasketPageLocators.CONTENT_TEXT)
        except NoSuchElementException as nex:
            assert False, f"{nex}\nNo empty message in basket page"

    def get_basket_items(self) -> list:
        return self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)


