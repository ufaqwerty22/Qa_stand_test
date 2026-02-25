from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.input_control import InputControl
from controls.button_control import ButtonControl


class LoginComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_login_input(self):
        return InputControl(self.page, self.wrapper.locator('[name="username"]'))

    def get_password_input(self):
        return InputControl(self.page, self.wrapper.locator('[name="password"]'))

    def get_submit_button(self):
        return ButtonControl(self.page, self.wrapper.locator('[type="submit"]'))