import pytest
from epyppeteer import launch


@pytest.mark.asyncio
async def async_gen_fixture():
    async with launch() as browser:
        page = await browser.newPage()
        await page.goto("https://example.com")
        await page.screenshot({"path": "image.png"})
