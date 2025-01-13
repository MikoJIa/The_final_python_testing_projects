import time

import pytest

from .pages.product_page import ProductPage


list_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

link_num = [link.split('/')[-1][-1] for link in list_links]


@pytest.mark.parametrize("links", [link for link in link_num])
def test_quest_can_add_product_to_basket(browser, links):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{links}"
    # if links == '7':
    #     return pytest.xfail(f"Skipping test {links}")
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.xfail_link(links)
    page.add_on_basket()
    time.sleep(2)
    page.calc_formula()
    page.price_product_in_basket_messages()
    page.name_product_in_basket_messages()



