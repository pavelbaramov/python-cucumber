Feature: Login Fail

    @login_fail
    Scenario: User cannot login with invalid password
        Given user is on the login page
        When user enters valid username "standard_use" and invalid password "invalid_password"
        Then the user is not logged in