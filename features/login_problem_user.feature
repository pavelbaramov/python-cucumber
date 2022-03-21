Feature: Login Problem User

    @login_problem_user
    Scenario: Log in to Sauce Lab with problem user
      Given user is on the login page
      When user enters valid username "problem_user" and valid password "secret_sauce"
      Then the user is logged in
