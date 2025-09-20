import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://weverse.io/")
    yield page
    context.close()
    browser.close()
    playwright.stop()