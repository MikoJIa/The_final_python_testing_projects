import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
#
#
# def test_quest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_quest_should_see_page_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()

    assert page.should_be_login_url() == "https://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_quest_should_be_substring_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()

    print(page.should_be_current_substring())
    assert page.should_be_current_substring() is True


def test_quest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_quest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()