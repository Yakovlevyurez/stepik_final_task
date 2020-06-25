from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self, driverr):
        self.should_be_login_url(driverr)
        self.should_be_login_form()
        self.should_be_register_form()

    @staticmethod
    def should_be_login_url(driverr):
        assert "login" in driverr.current_url, "wrong login url!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     m = driver.get(link)
#     a = driver.current_url
#     assert "logi" in a, "wrong login url!"
#     print(a)