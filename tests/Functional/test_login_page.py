import os

from playwright.sync_api import Page, expect

from pages import LoginPage


def test_valid_auth(page: Page):
    login_page = LoginPage(page)
    login_component = login_page.get_login_component()

    login_page.open()
    login_component.enter_username(os.getenv('VALID_USERNAME'))
    login_component.enter_password(os.getenv('VALID_PASSWORD'))
    login_component.click_submit_button()