Feature: Select a table from the list of available tables for export
  In order to export from a specific table
  As a user
  I want the webpage to allow me to select the table I wish to export from

  @Browser
  Scenario: I want to select 'table A'
    Given I go to "http://localhost:5000/"
    When I select "TableA" from "tables"
    Then the "TableA" option from "tables" should be selected

  @Browser
  Scenario: I want to select a table from a list of tables in a database
    Given I go to "http://localhost:5000/"
    When I select "DataTableC" from "tables"
    Then the "DataTableC" option from "tables" should be selected
