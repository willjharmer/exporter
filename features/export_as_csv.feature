Feature: Download export as a csv from the webpage
  In order to get a phyiscal copy of my export
  As a user
  I want the website to download a csv to my local machine

  @future
  Scenario: Export form validates and export downloads
    Given I have correctly filled out the export form
    When I click the download button
    Then an exported csv will download to my local machine
    And the export is named after the table i've exported from

  @future
  Scenario: Export form does not validate and so can't download
    Given I have incorrectly filled out the export form
    When I try to click the download button
    Then I find I can't download the export
    And I am told the fields that need to be corrected before I can download
