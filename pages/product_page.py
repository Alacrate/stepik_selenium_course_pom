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

    def should_be_add_product_message(self, product_name):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES_SUCCESS)
        assert len(messages) > 0, 'No success messsages'
        assert any(product_name == message.text for message in messages), f'Product name in basket is wrong or absent, expected {product_name}'

    def should_be_basket_price_messasge(self, price):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES_INFO)
        assert len(messages) > 0, 'No info messsages'
        assert any(price == message.text for message in messages), f'Basket price is wrong or absent, expected {price}'
