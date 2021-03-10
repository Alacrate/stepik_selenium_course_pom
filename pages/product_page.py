from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_product_message(self, expected_product_name):
        product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS_ADD_PRODUCT_NAME).text
        assert expected_product_name == product_name, f"Product name in basket is wrong or absent, expected '{expected_product_name}',got '{product_name}'"

    def should_be_basket_price_messasge(self, expected_price):
        price = self.browser.find_element(*ProductPageLocators.MESSAGE_INFO_NEW_BASKET_PRICE).text
        assert expected_price == price, f"Basket price is wrong or absent, expected '{expected_price}', got '{price}'"
