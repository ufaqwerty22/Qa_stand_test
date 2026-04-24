from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page: Page = page
        self.url: str = url

    async def open(self):
        await self.page.goto(self.url, wait_until='domcontentloaded')