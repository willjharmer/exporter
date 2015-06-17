from lettuce import step, world
from nose.tools import *
from app import AppFactory
from app.configs import Release, Dev, Test

@step(u'Given I have a (\w+) config object')
def given_i_have_a_config_object(step, config):
    world.config = eval(config)

@step(u'When I init app with the object')
def when_i_init_app_with_the_object(step):
    world.app = AppFactory.create(world.config)

@step(u'Then I have (\w+) DEBUG and (\w+) TESTING env variables')
def then_i_have_prescribed_debug_and_testing_env_variables(step, debug, testing):
    eq_(world.app.config['DEBUG'],eval(debug),'Debug config env var should equal {0}'.format(debug))
    eq_(world.app.config['TESTING'],eval(testing),'TESTING config env var should equal {0}'.format(testing))
