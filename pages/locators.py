from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn-group .btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".register_form #id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, ".register_form #id_registration-password1")
    CONFIRM_REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".register_form #id_registration-password2")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:first-child')
    ADD_TO_BACKED_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child strong')
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages .alert:last-child strong')
