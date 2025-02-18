
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url, wait_until="domcontentloaded")

    def fill_text(self,locator,text):
        self.page.locator(locator).fill(text)

    def click_element(self, locator):
        self.page.locator(locator).click()

    def get_text(self, locator):
        return self.page.locator(locator).text_content().strip()