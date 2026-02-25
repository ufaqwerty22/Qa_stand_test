import sys
import time

from playwright.sync_api import Page, expect

sys.path.append(r'C:\Users\PC\PycharmProjects\Qa_stand_test')
from pages.login_page import LoginPage


def test_login_page(page: Page):
    login_page = LoginPage(page)
    login_component = login_page.get_login_component()
    login_page.open()
    login_component.get_login_input().fill('qwerty123')
    login_component.get_password_input().fill('qwerty')
    login_component.get_submit_button().click_anyway()
    page.wait_for_timeout(4000)