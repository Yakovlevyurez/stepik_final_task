from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

main_page_link = "http://selenium1py.pythonanywhere.com"
login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page(driverr=browser)


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_url(browser):
    page = LoginPage(browser, login_page_link)
    page.open()
    page.should_be_login_url(driverr=browser)


def test_should_be_login_form(browser):
    page = LoginPage(browser, login_page_link)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    page = LoginPage(browser, login_page_link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, main_page_link)
    page.open()
    page.go_to_basket()
    page.is_checkout_btn_presented()
    page.is_basket_empty_mesage_presented()




