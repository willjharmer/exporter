Feature: I want to add clauses to my data export
  In order to get my desired subset of data in my exported csv
  As a user
  I want the webpage to allow me to add some clauses to filter the data in my export

  @future
  Scenario: I want to add a clause to my export
    Given I am on the export page and I have already selected an export table and some columns
    When I select the add clause button
    Then I get a suitable form for adding a clause to a column

  @future
  Scenario: I want to add a greater than 5 clause on a numeric column
    Given I am on the export page and I have already selected an export table
    And some columns
    And I've clicked the add clause button
    When I select the the clause column selection box
    Then I get see a list of available columns
    And I can select one of them

