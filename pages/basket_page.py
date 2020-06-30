from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def is_not_element_present_in_basket(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_element_present_in_basket(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_basket_empty_mesage_presented(self):
        assert self.is_element_present_in_basket(*BasketPageLocators.EMPTY_BASKET_MESSAGES), "Empty basket message is not presented"

    def is_checkout_btn_presented(self):
        assert self.is_not_element_present_in_basket(*BasketPageLocators.CHECKOUT_BTN), "Checkout button is not presented"




