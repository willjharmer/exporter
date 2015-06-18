Feature: Accessing the app through the web
  As a user
  In order to use the website I want to access the website via the web

  Scenario: Accessing the index page at '/'
    When I go to '/' route of the app
    Then I see the export web page

  Scenario: I see a web-form on the page
    When I go to '/' route of the app
    Then I can see a form

  Scenario: Accessing a bad route shows a 404 page
    When I go to '/this_route_does_not_exist' route of the app
    Then I see the 404 web page
    And there is a link back to the homepage

  #@wip
  #Scenario: When we have an internal error we display a 500 error page
    #When I POST to '/' route of the app
    #Then I see the 500 web page
    #And there is a link back to the homepage
