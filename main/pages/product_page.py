from main.pages.locators import ProductPageLocators
from main.pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def check_item_in_basket(self):
        item_name = self.get_product_name()
        item_price = self.get_product_price()

        item_name_in_alert = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_ALERT).text
        item_price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_ALERT).text

        assert item_name == item_name_in_alert, "selected and added to basket item name don't match"
        assert item_price == item_price_in_alert, "selected and added to basket item cost don't match"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_NAME_IN_ALERT),  "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_NAME_IN_ALERT), \
           "Success message is presented, but should not be"