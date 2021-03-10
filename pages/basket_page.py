from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "No text about empty basket, but should be"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM_SET), "Products are presence in basket, but should not be"
