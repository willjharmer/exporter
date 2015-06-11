Feature: Starting app with configuration
  In order to start the app with custom configuration
  As sysadmins
  We'll create a command line tool for configurable initilisation

  Scenario: Starting the app in * configuration
    Given I want to start the app in <config> configuration
    When I execute make <config> on command line
    Then manage.py receives the correct <command>

    Examples:
      |config  |command    |
      |test    |test       |
      |dev     |dev        |
      |release |run_server |
