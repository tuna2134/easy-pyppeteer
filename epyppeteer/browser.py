from pyppeteer.browser import Browser, BrowserContext
from pyppeteer.page import Page


async def newContext(self):
    obj = await self._connection.send('Target.createBrowserContext')
    browserContextId = obj['browserContextId']
    context = BrowserContext(self, browserContextId)  # noqa: E501
    self._contexts[browserContextId] = context
    return context

Browser.newContext = newContext
        
async def __aenter__(self) -> Page:
    return await self.newPage()
    
async def __aexit__(self, *args, **kwargs) -> None:
    await self.close()
    
BrowserContext.__aenter__ = __aenter__
BrowserContext.__aexit__ = __aexit__
