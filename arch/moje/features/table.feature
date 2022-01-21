Feature: Step Setup Table
  Scenario: Setup Table
     Given a set of specific users
      | name      | department   |
      | Jacek     | Szkolenia    |
      | Anna      | Comarch SA   |
      | Michał    | Comarch SA   |

    When we count the number of people in each department
    Then we will find two people in "Comarch SA"
    But we will find one person in "Szkolenia"