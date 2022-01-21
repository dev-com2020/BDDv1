#file: features/communication-with-server.feature

Feature: Introduction CV test
  The test verify if the communication with eCare and Bootstrap
  server works properly.
  @intro
  Scenario: Get token
    When We send "nomed-serv-get-token -s" to eCare
    Then We become server response "200"
  @intro
  Scenario: Keepalive test
    When We send "nomed-serv-keepalive" to eCare
    Then We become server response "200"
  @list
  Scenario: Get config
    Given List of config files

    |           name            |
    | MED_CARDIOVEST_CONFIG_DEV |
    | MED_CARDIOVEST_CONFIG_MED |
    | MED_CARDIOVEST_IMAGE_DOCK |
    | MED_CARDIOVEST_IMAGE_REC  |

    When We send "nomed-serv-get-config" to eCare
    Then We become server response "200"
    And We get list of config files
  @list
  Scenario: Upload config files on Bootstrap
    Given List of config files
    |           name            |   version  |
    | MED_CARDIOVEST_CONFIG_DEV |    None    |
    | MED_CARDIOVEST_CONFIG_MED |    None    |
    | MED_CARDIOVEST_IMAGE_DOCK | v1.2.1-20-g671d64d |
    | MED_CARDIOVEST_IMAGE_REC  | v1.2.0-4-g8f39410 |
    And Path to files ".\steps\files\"
    When We send files to Bootstrap
    Then We become server response "200"
  @list
  Scenario: Download config files from Bootstrap
    Given List of config files
    |           name            |   version  |
    | MED_CARDIOVEST_CONFIG_DEV |    None    |
    | MED_CARDIOVEST_CONFIG_MED |    None    |
    | MED_CARDIOVEST_IMAGE_DOCK | v1.2.1-20-g671d64d |
    | MED_CARDIOVEST_IMAGE_REC  | v1.2.0-4-g8f39410 |
    When We send files to device
    Then we become server response "200"
  @list
  Scenario: Detach config files from device
    Then We detach file from device