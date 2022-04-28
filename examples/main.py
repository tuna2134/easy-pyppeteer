import pytest
import asyncio
from epyppeteer import launch

@pytest.fixture
def test_setup():
    return asyncio.get_running_loop()

@pytest.mark.asyncio
async def test_use_browser(loop):
    async with launch() as browser:
        page = await browser.newPage()
        await page.goto("https://example.com")
        await page.screenshot({"path": "image.png"})
