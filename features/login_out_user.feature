Feature: Login_locked_out_user

  @login_locked_out_user
  Scenario: Log in to Sauce Lab
    Given user is on the login page
    When user enters valid username "locked_out_user" and valid password "secret_sauce"
    Then the user is locked out
