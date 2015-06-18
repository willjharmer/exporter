Feature: Select the columns that I want in my export
  In order to get my desired subset of data in my exported csv
  As a user
  I want the webpage to allow me to select a bunch of columns to include in export

  @future
  Scenario: I want only 'col 1, col 3, col 6' out of col 1 -> 10
    Given I am on the export page and I have already selected an export table
    When I select the column selection box
    Then I see the 10 avaialble columns
    And I am able to select only 'col 1, col 3, col 6'

  @future
  Scenario: By default I select all columns
    Given I am on the export page and I have already selected an export table
    When I make no selection in the column selection box
    Then by default all columns are selected

  @future
  Scenario: I select no columns
    Given I am on the export page and I have already selected an export table
    When I unselect all the columns in the column selection box
    Then I get an error message that tells me I must select some columns

