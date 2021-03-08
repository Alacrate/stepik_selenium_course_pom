from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=5) -> None:
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, element):
        try:
            self.browser.find_element(by, element)
        except NoSuchElementException:
            return False
        return True
