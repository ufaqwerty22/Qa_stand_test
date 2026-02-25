from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from components.info_component import InfoComponent
from components.login_component import LoginComponent


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://qa-stand-login.inzhenerka.tech/login')

    def get_info_component(self):
        return InfoComponent(self.page, self.page.locator('(//div[contains(@class, "shadow")])[1]'))

    def get_login_component(self):
        return LoginComponent(self.page, self.page.locator('.card-body'))