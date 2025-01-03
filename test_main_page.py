from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:

    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


    def test_quest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        go_to_login_page(browser)