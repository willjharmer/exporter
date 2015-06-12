Feature: Web application for exporting data
  As an analyst 
  I wish to be able to visit a web application
  and export data from a database

  Background:
    Given I access the web app from a browser

  Scenario: User visits "/" route of web app
    When I go to the "/" route
    Then I get a 200 status
    And I get a web page with the title "Exporter"

  #Scenario: User visits a page that doesn't exist
    #When I go to the "this_does_not_exist" route
    #Then I get a 404 status
    #And I get a friendly explanation of the error
    #And I get a url to redirect me to the homepage
