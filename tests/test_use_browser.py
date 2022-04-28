import pytest
from epyppeteer import launch


@pytest.mark.asyncio
async def test_use_browser():
    print("take example.com")
    async with launch() as browser:
        page = await browser.newPage()
        await page.goto("https://example.com")
        print(await page.title())
        await page.screenshot({"path": "example.png"})
