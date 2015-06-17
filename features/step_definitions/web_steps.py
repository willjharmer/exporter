from lettuce import step, world
from nose.tools import *
from app import AppFactory

@step(u'Given I have a web browser')
def given_i_have_a_web_browser(step):
    assert False, 'This step must be implemented'

@step(u'When I go to \'([^\']*)\' route of the app')
def when_i_go_to_group1_route_of_the_app(step, group1):
    assert False, 'This step must be implemented'

@step(u'Then I see the expected web page')
def then_i_see_the_expected_web_page(step):
    assert False, 'This step must be implemented'
