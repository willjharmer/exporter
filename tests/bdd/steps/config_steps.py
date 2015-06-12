# -*- coding: utf-8 -*-

from lettuce import step, world
from nose.tools import *

@step(u'I init app with a (.*) config object')
def having_a_config_config_object(step, config):
    world.config = config

@step(u'I have (.*) DEBUG and (.*) TESTING env variables')
def expect_debug_and_testing_env_variables(step,debug,testing):
    ok_(False, "d={0} t={1}".format(debug, testing))
