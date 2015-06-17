Feature: Accessing the app through the web
  As a user
  In order to use the website I want to access the website via the web 

  Scenario: Accessing the index page at '/'
    Given I have a web browser
    When I go to '/' route of the app
    Then I see the expected web page
