Feature: Multiple item checkout

  @multiple_item_checkout
  Scenario: Log in to Sauce Lab and select multiple item to the shopping card
    Given user is on the login page
    When user enters valid username "standard_user" and valid password "secret_sauce"
    Then user selects multiple items from the product list

  Scenario: Validate multiple items are added to the shopping card
    Given validate selected multiple items from the product list are in the shopping card
    Then user enters first_name "pavel" and last_name "baramov" and postal_code "1415"
    But user is at the checkout overview page and observes the selected items and finish the order
     And the user is logged in
