Feature: Select a database from the list of available databases for export
  In order to export from a specific database
  As a user
  I want the webpage to allow me to select the database I wish to export from

  @future
  Scenario: I want to select database 'datalab'
    Given I am on the export webpage
    When I click on the database list select box
    Then I get a list of all the available databases
    And I can select one of them
