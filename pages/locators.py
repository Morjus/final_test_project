from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[value="Log In"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')
    REG_EMAIL_INPUT = (
        By.CSS_SELECTOR, 'input[type="email"][name="registration-email"]')
    REG_PASSWORD_INPUT = (
        By.CSS_SELECTOR, 'input[type="password"][name="registration-password1"]')
    REG_REPEAT_PASSWORD = (
        By.CSS_SELECTOR, 'input[type="password"][name="registration-password2"]')
    REGISTRATION_SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_COST = (By.CSS_SELECTOR, ".col-sm-6.product_main  p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main :nth-child(1)")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner :first-child")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    CART_COST = (By.CSS_SELECTOR, ".alert-info .alertinner :nth-last-child(1)")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR,
                   '.btn-group .btn.btn-default[href$="basket/"]')
    BASKET_LINK_INVALID = (
        By.CSS_SELECTOR, '.btn-group .btn.btn-default[href^="basket/"]')
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
