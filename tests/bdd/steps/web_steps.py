# -*- coding: utf-8 -*-

from lettuce import *
from nose.tools import *
from bs4 import BeautifulSoup
from app.app import app

@step(u'Given I access the web app from a browser')
def access_the_web_page_from_a_browser(step):
    world.app = app.test_client()

@step(u'I go to the "([^"]*)" route')
def go_to_route(step, route):
    world.browser = world.app.get(route)

@step(u'Then I get a (.*) status')
def get_given_status(step, status):
    eq_(world.browser.status_code, int(status))

@step(u'And I get a web page with the title "(.*)"')
def get_page_with_given_title(step, title):
    html = world.browser.get_data() 
    page = BeautifulSoup(html)
    title_tag = page.title
    eq_(title_tag.contents[0], title)

#@step(u'And I get a friendly explanation of the error')
#def get_friendly_explanation(step):

#@step(u'And I get a url to redirect me to the homepage')
#def url_back_to_homepage_present(step):

