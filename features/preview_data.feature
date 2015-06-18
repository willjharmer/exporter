Feature: Preview the data before I download it
  In order to have some idea of the data I'm going to export
  As a user
  I want the webpage to show me a preview table of the data I will be exporting

  @future
  Scenario: I have just selected a table from the table selection box
    Given I am on the export webpage
    When I select 'table A' from the table selection box
    Then I see the preview table updating showing a preview of the data
    And that preview is 5 rows
    And that preview shows all the columns

  @future
  Scenario: I have just selected a list of columns from the column selection box
    Given I am on the export webpage
    When I select 'col 1, col 3, col 6' from the column selection box
    Then I see the preview table updating showing a preview of the newly filtered data subset
    And that preview is 5 rows
    And that preview shows only the columns selected

  @future
  Scenario: I have added clauses to my export form
    Given I am on the export webpage
    When I add the clause 'col 3 > 5' in the export form
    Then I see the preview table updating showing a preview of the newly filtered data subset
    And that preview is 5 rows
    And that preview shows only rows where 'col 3 > 5'
