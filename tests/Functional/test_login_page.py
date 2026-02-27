import sys

from playwright.sync_api import Page, expect

sys.path.append(r'C:\Users\PC\PycharmProjects\Qa_stand_test')
from pages.login_page import LoginPage


def test_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('testuser')
    login_page.enter_password('password123')
    login_page.click_submit_button()