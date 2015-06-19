from lettuce import step, world
from nose.tools import *
from selenium import webdriver
from utils import TestServer

@step(u'Given I am on the export webpage')
def given_i_am_on_the_export_webpage(step):
    world.server = TestServer().get_server_url()
    world.driver = webdriver.PhantomJS()
    world.driver.set_window_size(1120, 550)
    world.driver.get(world.server)

@step(u'When I click on the table list select box')
def when_i_click_on_the_table_list_select_box(step):
    assert False, 'This step must be implemented'

@step(u'Then I get a list of all the available tables')
def then_i_get_a_list_of_all_the_available_tables(step):
    assert False, 'This step must be implemented'

@step(u'And I can select one of them')
def and_i_can_select_one_of_them(step):
    assert False, 'This step must be implemented'
