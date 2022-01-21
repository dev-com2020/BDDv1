Feature: calculating vat

  Scenario Outline: create product
    Given I created product called <name> with the price <price> and VAT <vat_rate>
    Then the vat value will be <vat_value>

    Examples: Products with 23%
      | name          | price | vat_rate | vat_value |
      | Mobile        | 1230  | 23       | 230.00    |
      | Computer      | 3600  | 23       | 673.17    |
      | Notebook      | 7999  | 23       | 1495.75   |

    Examples: Products with 5%
      | name             | price  | vat_rate | vat_value |
      | How to be rich?  | 29.99  | 5        | 1.43      |
      | Done Definitions | 59.99  | 5        | 2.86      |
      | Motivation       | 75.99  | 5        | 3.62      |

    Examples: Products with 8%
      | name  | price  | vat_rate | vat_value |
      | Bolt  | 24.89  | 8        | 1.84      |
      | Uber  | 31.34  | 8        | 2.32      |