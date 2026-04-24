from playwright.async_api import Page, Locator

from controls.base_control import BaseControl


class InputControl(BaseControl):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    async def fill(self, text: str):
        await self.wrapper.fill(text)

    async def clear_and_fill(self, text: str):
        await self.wrapper.clear()
        await self.wrapper.fill(text)