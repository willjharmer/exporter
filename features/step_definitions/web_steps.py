from lettuce import step, world
from nose.tools import *

@step(u'When I go to \'([^\']*)\' route of the app')
def when_i_go_to_specified_route_of_the_app(step, route):
    world.visit(route)

@step(u'Then I see the export web page')
def then_i_see_the_expected_web_page(step):
    eq_(world.page_response.title.string, 'Exporter')

@step(u'Then I can see a form')
def then_i_see_a_form(step):
    ok_(world.page_response.form is not None)

@step(u'Then I see the 404 web page')
def then_i_see_404_page(step):
    eq_(world.page_response.title.string, 'Page not found - Exporter')

@step(u'And there is a link back to the homepage')
def there_is_a_link_back_to_homepage(step):
    eq_(len(world.page_response.find("a", { "href" : "/"})), 1)

#@step(u'When I POST to \'([^\']*)\' route of the app')
#def when_i_post_to_specified_route_of_the_app(step, route):
    #data = dict(name="RandomData")
    #world.post(route, data)

#@step(u'Then I see the 500 web page')
#def then_i_see_500_page(step):
    #eq_(world.page_response.title.string, 'Something went wrong - Exporter')


