from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.input_control import InputControl
from controls.button_control import ButtonControl


class LoginComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__username_input = InputControl(self.page, self.wrapper.locator('[name="username"]'))
        self.__password_input = InputControl(self.page, self.wrapper.locator('[name="password"]'))
        self.__submit_button = ButtonControl(self.page, self.wrapper.locator('[type="submit"]'))

    def get_username_input(self):
        return self.__username_input

    def get_password_input(self):
        return self.__password_input

    def get_submit_button(self):
        return self.__submit_button

    def enter_username(self, username):
        self.__username_input.fill(username)

    def enter_password(self, password):
        self.__password_input.fill(password)

    def click_submit_button(self):
        self.__submit_button.click_anyway()