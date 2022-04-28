from pyppeteer.browser import Browser as OldBrowser, BrowserContext as OldBrowserContext
from pyppeteer.page import Page


class Browser(OldBrowser):
    
    async def newContext(self):
        obj = await self._connection.send('Target.createBrowserContext')
        browserContextId = obj['browserContextId']
        context = BrowserContext(self, browserContextId)  # noqa: E501
        self._contexts[browserContextId] = context
        return context

        
class BrowserContext(OldBrowserContext):
    async def __aenter__(self) -> Page:
        return await self.newPage()
    
    async def __aexit__(self, *args, **kwargs) -> None:
        await self.close()
 

OldBrowserContext = BrowserContext
OldBrowser = Browser
