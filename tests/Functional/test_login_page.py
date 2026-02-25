import sys

from playwright.sync_api import Page, expect

sys.path.append(r'C:\Users\PC\PycharmProjects\Qa_stand_test')
from pages.login_page import LoginPage


def test_login_page(page: Page):
    login_page = LoginPage(page)
    login_component = login_page.get_login_component()
    login_page.open()
    page.wait_for_timeout(2500)
    login_component.login('qwerty', 'qwerty')