import os

from playwright.async_api import Page, expect

from pages import LoginPage


async def test_valid_auth(page: Page):
    login_page = LoginPage(page)
    login_component = login_page.get_login_component()

    await login_page.open()
    await login_component.enter_username(os.getenv('VALID_USERNAME'))
    await login_component.enter_password(os.getenv('VALID_PASSWORD'))
    await login_component.click_submit_button()