from pyppeteer.browser import BrowserContext
from pyppeteer.page import Page
        
async def __aenter__(self) -> Page:
    return await self.newPage()
    
async def __aexit__(self, *args, **kwargs) -> None:
    await self.close()
    
BrowserContext.__aenter__ = __aenter__
BrowserContext.__aexit__ = __aexit__
