import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, url)
        page.open()
        email = str(time.time())+'@example999.com'
        password = 'padfgsssdfgwo6786rd'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        product_name = page.get_product_name()
        product_price =  page.get_product_price()
        page.add_to_basket()
        page.should_be_add_product_message(product_name)
        page.should_be_basket_price_messasge(product_price)

urls = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}' for i in range(10)]
urls[7] = (pytest.param(urls[7], marks=pytest.mark.xfail(reason='offer7 is bugged'))) # type: ignore

@pytest.mark.need_review
@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    product_name = page.get_product_name()
    product_price =  page.get_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_product_message(product_name)
    page.should_be_basket_price_messasge(product_price)

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_text()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url, timeout=0)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()
