from pyppeteer.launcher import Launch
from pyppeteer.browser import Browser
from typing import Any

class launch:
    def __init__(self, options: dict, **kwargs: Any):
        self.__kwargs = kwargs
        self.__options = options
        self.__browser: Browser = None
            
    @property
    def browser(self) -> Browser:
        return self.__browser
        
    async def __aenter__(self) -> Browser:
        self.browser = await Launch().launch(self.__options, **self.__kwargs)
        return self.browser
    
    async def __aexit__(self, *args, **kwargs):
        await self.browser.close()
