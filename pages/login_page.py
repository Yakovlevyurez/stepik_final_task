from .base_page import BasePage
from .locators import LoginPageLocators
import time


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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        pass2_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REG_BUTTON)
        register_button.click()
        time.sleep(5)







# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#     m = driver.get(link)
#     a = driver.current_url
#     assert "logi" in a, "wrong login url!"
#     print(a)