Feature: Select a table from the list of available tables for export
  In order to export from a specific table
  As a user
  I want the webpage to allow me to select the table I wish to export from

  @future
  Scenario: I want to select 'table A'
    Given I am on the export webpage
    When I click on the table list select box
    Then I get a list of all the available tables
    And I can select one of them 
