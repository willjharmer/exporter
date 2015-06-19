from app import AppFactory
import multiprocessing 
import time

class TestServer():

    def create_app(self):
        return AppFactory.create()

    def __init__(self):
        """
        Does the required setup, doing it here means you don't have to
        call super.setUp in subclasses.
        """

        # Get the app
        self.app = self.create_app()

        # We need to create a context in order for extensions to catch up
        self._ctx = self.app.test_request_context()
        self._ctx.push()

        try:
            self._spawn_live_server()
        finally:
            self.teardown()
            self.terminate_live_server()

    def get_server_url(self):
        """
        Return the url of the test server
        """
        return 'http://localhost:%s' % self.port

    def _spawn_live_server(self):
        self._process = None
        self.port = self.app.config.get('LIVESERVER_PORT', 5000)

        worker = lambda app, port: app.run(port=port, use_reloader=False)

        self._process = multiprocessing.Process(
            target=worker, args=(self.app, self.port)
        )

        self._process.start()

        # we must wait for the server to start listening with a maximum timeout of 5 seconds
        timeout = 5
        while timeout > 0:
            time.sleep(1)
            try:
                urlopen(self.get_server_url())
                timeout = 0
            except:
                timeout -= 1

    def teardown(self):
        if getattr(self, '_ctx', None) is not None:
            self._ctx.pop()
            del self._ctx

    def terminate_live_server(self):
        if self._process:
            self._process.terminate() 
