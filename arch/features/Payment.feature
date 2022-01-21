Feature: Payment Types

   Scenario: Verify user has two payment options
      Given User is on Payment screen
      When User clicks on Payment types
      Then User should get Cash

      @drugi
   Scenario: Verify user has one payment options
      Given User is on Payment screen
      When User clicks on Payment types
      Then User should get Cash