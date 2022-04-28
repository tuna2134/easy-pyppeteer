# easy-pyppeteer

## install

```python
pip install epyppeteer
```

## sample code

```python
from epyppeteer import launch
import asyncio

async def main():
    async with launch() as browser:
        page = await browser.newPage()
        await page.goto("https://example.com")
        await page.screenshot({"path": "image.png"})
        
asyncio.run(main())
```
