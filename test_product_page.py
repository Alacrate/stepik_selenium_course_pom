import pytest

from .pages.product_page import ProductPage

urls = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}' for i in range(10)]
urls[7] = (pytest.param(urls[7], marks=pytest.mark.xfail(reason='offer7 is bugged'))) # type: ignore

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

@pytest.mark.xfail
@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_guest_cant_see_success_message(browser, url):
    page = ProductPage(browser, url, timeout=0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_message_disappeared_after_adding_product_to_basket(browser, url):
    page = ProductPage(browser, url, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()
