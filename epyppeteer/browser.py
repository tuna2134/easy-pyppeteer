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
        
    async def launch(self) -> Browser:  # noqa: C901
        """Start chrome process and return `Browser` object."""
        self.chromeClosed = False
        self.connection: Optional[Connection] = None

        options = dict()
        options['env'] = self.env
        if not self.dumpio:
            # discard stdout, it's never read in any case.
            options['stdout'] = subprocess.DEVNULL
            options['stderr'] = subprocess.STDOUT

        self.proc = subprocess.Popen(  # type: ignore
            self.cmd, **options, )

        def _close_process(*args: Any, **kwargs: Any) -> None:
            if not self.chromeClosed:
                self._loop.run_until_complete(self.killChrome())

        # don't forget to close browser process
        if self.autoClose:
            atexit.register(_close_process)
        if self.handleSIGINT:
            signal.signal(signal.SIGINT, _close_process)
        if self.handleSIGTERM:
            signal.signal(signal.SIGTERM, _close_process)
        if not sys.platform.startswith('win'):
            # SIGHUP is not defined on windows
            if self.handleSIGHUP:
                signal.signal(signal.SIGHUP, _close_process)

        connectionDelay = self.slowMo
        self.browserWSEndpoint = get_ws_endpoint(self.url)
        logger.info(f'Browser listening on: {self.browserWSEndpoint}')
        self.connection = Connection(self.browserWSEndpoint, self._loop, connectionDelay, )
        browser = await Browser.create(self.connection, [], self.ignoreHTTPSErrors, self.defaultViewport, self.proc,
                                       self.killChrome)
        await self.ensureInitialPage(browser)
        return browser
        
    
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
