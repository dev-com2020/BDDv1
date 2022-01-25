@test-data-from-excel
  Feature: Examples table with data test
    Scenario Outline: Test
      When I visit the URL <base>/<page>/<ordNumber>/<custName>
      Then the browser contains test <custNumber>

      Examples:
      |base                 | page|ordNumber|custName|


