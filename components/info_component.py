from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.link_control import LinkControl


class InfoComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_link_by_text(self, text):
        return LinkControl(self.page, self.wrapper.get_by_text(text))

    def click_link_by_text(self, text):
        self.get_link_by_text(text).click_anyway()