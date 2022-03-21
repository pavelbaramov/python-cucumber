Feature: Login

  @login
  Scenario: Log in to Sauce Lab
    Given user is on the login page
    When user enters valid username "standard_user" and valid password "secret_sauce"
    Then the user is logged in
