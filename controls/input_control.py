from playwright.sync_api import Page, Locator

from controls.base_control import BaseControl


class InputControl(BaseControl):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def fill(self, text: str):
        self.wrapper.fill(text)

    def clear_and_fill(self, text: str):
        self.wrapper.clear()
        self.wrapper.fill(text)