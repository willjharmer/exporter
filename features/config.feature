Feature: Configuring flask app
  In order to have custom environment configurations
  As developers
  We'll allow app initialisation with a config object

  Scenario: Configuring application
    Given I have a <config> config object
    When I init app with the object
    Then I have <debug> DEBUG and <testing> TESTING env variables

    Examples:
      |config |debug  | testing |
      |Base   |False  |False    |
      |Dev    |True   |False    |
      |Test   |False  |True     |

