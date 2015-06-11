from lettuce import step, world
from nose.tools import *

@step('Given I have a <config> config object')
def given_i_have_a_config_config_object(step, config):
    world.config = config

@step(u'When I init app with the object')
def when_i_init_app_with_config_object(step):
    world.app.config = world.config

@step(u'Then I have <debug> DEBUG and <testing> TESTING env variables')
def then_i_have_debug_debug_and_testing_testing_env_variables(step):
    eq_('pass', 'This step must be implemented')



