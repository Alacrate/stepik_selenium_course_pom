class BasePage:
    def __init__(self, browser, url, timeout=5) -> None:
        self.browser = browser
        self.browser.implicity_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)
