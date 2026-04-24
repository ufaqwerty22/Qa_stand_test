import pytest_asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
load_dotenv()


@pytest_asyncio.fixture(scope='function')
async def page():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch()
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()
    yield page
    await browser.close()
    await playwright.stop()
