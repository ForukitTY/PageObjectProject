from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, language="ru"):
        self.should_be_login_url(language=language)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, language):
        # реализуйте проверку на корректный url адрес
        # http://selenium1py.pythonanywhere.com/ru/accounts/login/
        assert self.browser.current_url == f"http://selenium1py.pythonanywhere.com/{language}/accounts/login/"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)