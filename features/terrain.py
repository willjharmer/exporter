from lettuce import before, after, world
from app import AppFactory
from app.configs import Test
from BeautifulSoup import BeautifulSoup

@before.each_scenario
def setup_client(scenario):
    app = AppFactory.create(Test)
    world.client = app.test_client()

@world.absorb
def visit(route):
    world.raw_response = world.client.get(route)
    world.page_response = BeautifulSoup(world.raw_response.data)

@world.absorb
def post(route, data):
    world.raw_response = world.client.post(route, data, follow_redirects=True)
    world.page_response = BeautifulSoup(world.raw_response.data)
