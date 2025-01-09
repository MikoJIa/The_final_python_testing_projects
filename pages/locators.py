from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators():
    BUTTON_ADD_ON_BASKET = (By.XPATH, "//form/button[@value='Добавить в корзину']")
    MESSAGE_ABOUT_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, "div.alertinner")
    LINK_BASKET = (By.CSS_SELECTOR, "a.btn.btn-info.btn-sm")
    NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    NAME_PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "p.price_color")
