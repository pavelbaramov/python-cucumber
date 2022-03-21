Feature: Login Performance Glitch User

    @login_performance_glitch_user
    Scenario: Log in to Sauce Lab with problem user
      Given user is on the login page
      When user enters valid username "performance_glitch_user" and valid password "secret_sauce"
      Then the user is logged in
