Feature: Payment Module
  Scenario: Verify message after payment
    Given User is on payment screen
    When User enters payment detail
    And User completes payment
    Then User should get success message

    Scenario: Verify new users can process payment
      Given User keys in payment info and submits
      Then success message should get displayed

