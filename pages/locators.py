from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[href*=basket]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_FORM_SET = (By.ID, 'basket_formset')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    MESSAGE_SUCCESS_ADD_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    MESSAGE_INFO_NEW_BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p strong')
    MESSAGES_SUCCESS = (By.CSS_SELECTOR, '#messages .alert-success')
    MESSAGES_INFO = (By.CSS_SELECTOR, '#messages .alert-info')
