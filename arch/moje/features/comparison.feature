
Feature: Step Result Table

  Scenario: Unordered Result Table Comparison (RowFixture Table)

    Given a set of specific users
      | name      | department   |
      | Jacek     | Szkolenia    |
      | Anna      | Comarch SA   |
      | Michał    | Comarch SA   |

    Then we will have the following people in "Comarch SA":
      | name      |
      | Anna      |
      | Michał    |
    And we will have the following person in "Szkolenia":
      | name      |
      | Jacek     |

    Scenario: Subset Result Table Comparison
      Given a set of specific users
      | name      | department   |
      | Zbyszek   | Orange       |
      | Tomek     | Orange       |
      Then we will have at least the following people in "Orange":
      | name      |
      | Zbyszek   |
      