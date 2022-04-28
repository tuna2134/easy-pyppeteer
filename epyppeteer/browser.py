from pyppeteer.launcher import Launcher
from pyppeteer.browser import Browser


class launch(Launcher):
    @property
    def browser(self) -> Browser:
        return self.__browser
        
    async def __aenter__(self) -> Browser:
        self.__browser = await self.launch()
        return self.__browser
    
    async def __aexit__(self, *args, **kwargs):
        await self.__browser.close()
