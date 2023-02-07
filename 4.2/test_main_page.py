import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_can_go_to_login_page(browser,language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")