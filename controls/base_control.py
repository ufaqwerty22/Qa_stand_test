from playwright.async_api import Page, Locator


class BaseControl:
    def __init__(self, page: Page, wrapper: Locator):
        self.page: Page = page
        self.wrapper: Locator = wrapper

    async def click_anyway(self):
        await self.wrapper.click(force=True)