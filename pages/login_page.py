from .base_page import BasePage
from .main_page import MainPage
from .locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.common.by import By



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        return login_url.get_attribute("href")

    def should_be_current_substring(self):
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        cur_url = login_url.get_attribute('href')
        print(cur_url)
        return self.curr_url(cur_url)

    def should_be_login_form(self):
        login_page = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_page.click()

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        register_page = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        register_page.click()

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
