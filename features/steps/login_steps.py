from behave import *
from nose.tools import assert_true


# navigate to Sauce Demo using the url set in login_page.py
# if title is 'Swaglabs' then navigation was successful
@given('user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_sauce_lab()


# valid username and valid password parameters are set in login.feature
@when('user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


# valid username and invalid password parameters are set in login.feature
@when('user enters valid username "{username}" and invalid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('user selects multiple items from the product list')
def step_impl(context):
    context.products_page.multiple_item_selection()


@then('validate selected multiple items from the product list are in the shopping card')
def step_impl(context):
    context.products_page.shopping_card()


@then('user enters first_name "{first_name}" and last_name "{last_name}" and postal_code "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    context.products_page.checkout_personal_data(first_name, last_name, postal_code)


@then('user is at the checkout overview page and observes the selected items and finish the order')
def step_impl(context):
    context.products_page.checkout_overview_validation()
    context.products_page.checkout_finish()


# if the user can access the account button and sign out then they are logged in
@then('the user is logged in')
def step_impl(context):
    context.products_page.logout()


# if the invalid password error appears an invalid password was entered
@then('the user is not logged in')
def step_impl(context):
    context.login_page.get_login_error()


# if the user is locked out an error message for locked out user appears
@then('the user is locked out')
def step_impl(context):
    context.login_page.get_login_locked_out_error()
