import pytest

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):


    def add_on_basket(self):
        button_add_on_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_ON_BASKET)
        button_add_on_basket.click()


    def price_product_in_basket_messages(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_product_in_messages = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text

        assert price_product == price_product_in_messages, 'There is no such product price in the cart'


    def name_product_in_basket_messages(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_messages = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_MESSAGE).text

        assert name_product == name_product_messages, 'There is no such product in the shopping cart'
