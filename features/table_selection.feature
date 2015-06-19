Feature: Select a table from the list of available tables for export
  In order to export from a specific table
  As a user
  I want the webpage to allow me to select the table I wish to export from

  @wip
  @TestServer
  Scenario: I want to select 'table A'
    Given I go to "http://localhost:5000/"
    When I select "Table A" from "tables"
    Then the "Table A" option from "tables" should be selected
