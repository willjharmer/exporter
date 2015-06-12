Feature: Configuring flask app
  We'll allow app initialisation with a config object so that
  As a developer
  I can have custom environment configurations

  Scenario: Configuring application
    Given I init app with a <config> config object
    Then I have <debug> DEBUG and <testing> TESTING env variables

    Examples:
      |config |debug  | testing |
      |Base   |False  |False    |
      |Dev    |True   |False    |
      |Test   |False  |True     |

