import time

from .pages.product_page import ProductPage


def test_quest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_on_basket()
    time.sleep(2)
    page.calc_formula()
    page.price_product_in_basket_messages()
    page.name_product_in_basket_messages()


