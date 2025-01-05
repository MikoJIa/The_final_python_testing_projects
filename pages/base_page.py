from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def curr_url(self, curr_substring):
        # get_url = self.browser.current_url
        # sub_str_url = get_url.split('/')[-1]
        # if sub_str_url == curr_substring.split('/')[-1]:
        sub_str = curr_substring.find("login")
        if sub_str != -1:
            return True
        return False

