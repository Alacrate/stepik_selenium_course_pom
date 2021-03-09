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
