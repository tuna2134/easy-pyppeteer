from pyppeteer.launcher import Launcher
from pyppeteer.browser import Browser as OldBrowser, BrowserContext as OldBrowserContext
from pyppeteer.page import Page


class launch(Launcher):
    @property
    def browser(self) -> Browser:
        return self.__browser
        
    async def __aenter__(self) -> Browser:
        self.__browser = await self.launch()
        return self.__browser
    
    async def __aexit__(self, *args, **kwargs) -> None:
        await self.__browser.close()
        
    
class Browser(OldBrowser):
    @staticmethod
    async def create(connection: Connection, contextIds: List[str],
                     ignoreHTTPSErrors: bool, defaultViewport: Optional[Dict],
                     process: Optional[Popen] = None,
                     closeCallback: Callable[[], Awaitable[None]] = None,
                     **kwargs: Any) -> "Browser":
        """Same."""
        browser = Browser(connection, contextIds, ignoreHTTPSErrors,
                          defaultViewport, process, closeCallback)
        await connection.send('Target.setDiscoverTargets', {'discover': True})
        return browser
    
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
