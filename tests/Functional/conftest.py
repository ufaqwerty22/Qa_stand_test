import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()


@pytest.fixture(scope='function')
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()
