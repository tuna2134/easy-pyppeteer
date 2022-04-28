from pyppeteer import launch as oldlaunch
from pyppeteer.browser import Browser

class launch:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.browser: Browser = None
        
    async def __aenter__(self) -> Browser:
        self.browser = await oldlaunch(*self.args, **self.kwargs)
        return self.browser
    
    async def __aexit__(self, *args, **kwargs):
        await self.browser.close()
