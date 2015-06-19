Feature: Accessing the app through the web
  As a user
  In order to use the website I want to access the website via the web

  @Browser
  Scenario: Accessing the index page at '/'
    When I visit "http://localhost:5000/" 
    Then I should see "Exporter"

  @Browser
  Scenario: I see a web-form on the page
    When I visit "http://localhost:5000/" 
    Then I should see a form that goes to "/export"

  @Browser
  Scenario: Accessing a bad route shows a 404 page
    When I visit "http://localhost:5000/random_route" 
    Then I should see "404 web page"
    And I should see a link with the url "/"

  #@wip
  #Scenario: When we have an internal error we display a 500 error page
    #When I POST to '/' route of the app
    #Then I see the 500 web page
    #And there is a link back to the homepage
