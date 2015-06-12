Feature: Starting app with configuration
  As a sysadmin
  I want to be able to start the app with a custom configuration
  from the command line

  Scenario: Starting the app in * configuration
    Given I want to start the app in <config> configuration
    When I execute make <config> on command line
    Then manage.py receives the correct <command>

    Examples:
      |config  |command    |
      |test    |test       |
      |dev     |dev        |
      |release |run_server |
