from test import *

class MyTest(TestCase):
    def create_app(self):

        return AppFactory.create()

    def test_app_config(self):
        ok_(True)

    def test_that_fails(self):
        ok_(False)
