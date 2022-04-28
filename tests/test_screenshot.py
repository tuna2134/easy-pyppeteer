import pytest
import asyncio
from epyppeteer import launch

@pytest.mark.asyncio
async def test_use_browser():
    async with launch() as browser:
        page = await browser.newPage()
        await page.goto("https://example.com")
        await page.screenshot({"path": "example.png"})
