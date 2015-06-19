from lettuce import before, after, world
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from utils import TestServer
import lettuce_webdriver.webdriver

@before.all
def setup_server():
    world.server = TestServer()

@after.all
def teardown_server(total):
    world.server.teardown()
    world.server.terminate_live_server()

@before.each_scenario
def setup_client(scenario):
    world.browser = webdriver.PhantomJS()
    world.browser.set_window_size(1120, 550)

@after.each_scenario
def teardown_client(scenario):
    world.browser.quit()

@world.absorb
def visit(route):
    world.url = world.server.get_server_url() + route
    world.browser.get(world.url)
    world.page_response = BeautifulSoup(world.browser.page_source)
