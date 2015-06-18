from test import *

class WebTests(TestCase):
    
    render_templates = False

    def create_app(self):
        return AppFactory.create()

    def test_that_index_route_is_ok(self):
        response = self.client.get('/')
        self.assert200(response)

    def test_that_index_route_uses_index_template(self):
        response = self.client.get('/')
        self.assert_template_used('index.haml')

    def test_that_dodgy_route_gets_404(self):
        response = self.client.get('/route_that_does_not_exist')
        self.assert404(response)

    def test_that_phony_route_uses_404_template(self):
        response = self.client.get('route_that_does_not_exist')
        self.assert_template_used('errors/404.haml')

    #TODO - Test a 500 error handler
