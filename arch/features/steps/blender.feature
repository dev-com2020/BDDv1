# -*- coding: UTF-8 -*-

Feature: Scenario Outline
  Scenario Outline: Blenders
    Given I put <thing> in a blender
    When I switch the blender on
    Then Is should transform into <other_thing>

    Examples: Amphibians
      | thing         | other_thing |
      | Red Tree Frog | mush        |
      | apples        | apple juice |

    Examples: Consumer Electronics
    | thing         | other_thing |
    | iPhone        | toxic waste |
    | Galaxy Nexus  | toxic waste |
