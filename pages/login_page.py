from playwright.async_api import Page, Locator

from pages.base_page import BasePage
from components.info_component import InfoComponent
from components.login_component import LoginComponent


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://qa-stand-login.inzhenerka.tech/login')
        self.__info_component = InfoComponent(self.page, self.page.locator('(//div[contains(@class, "shadow")])[1]'))
        self.__login_component = LoginComponent(self.page, self.page.locator('.card-body'))

    def get_info_component(self):
        return self.__info_component

    def get_login_component(self):
        return self.__login_component