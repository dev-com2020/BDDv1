Feature: User info
  Scenario: Check login
    Given Collection of credentials

      | username | password |
      | admin    |  12345   |
      | user1    |  pwd1    |
      | user2    |  pwd2    |

    Then user should be logged in


