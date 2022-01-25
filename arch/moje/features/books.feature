Feature: A Step uses a User-Defined Type as Step Parameter

   Scenario Outline: Search site
    Given I visit <site>
        | site     |
        |  api1    |
        |  api1    |
        |  api2    |
        |  api2    |
    When I entered <search_int>
    Then I see 1 result

     Examples:
        | search_int
        |  1 |
        |  2 |
        |  1 |
        |  7 |
     
