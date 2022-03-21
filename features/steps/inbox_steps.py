from behave import *
from nose.tools import assert_true


# if title is 'Inbox' then user is on the inbox page
@given('user is on the inbox page')
def step_impl(context):
    context.product_page.assert_login_success()


@step('user navigates to inbox page')
def step_impl(context):
    context.product_page.navigate_to_inbox()


@step('user composes a message with '
      'recipient "{recipient}" and '
      'subject "{subject}" and '
      'message "{message}"'
      )
def step_impl(context, recipient, subject, message):
    context.product_page.compose_message(recipient, subject, message)


# @step('user sends message')
# def step_impl(context):
#     context.inbox_page.send_message()


@step('the message is sent successfully')
def step_impl(context):
    context.product_page.message_sent_assert()


@when('user deletes the message')
def step_impl(context):
    context.product_page.delete_message()


@then('the message is successfully deleted')
def step_impl(context):
    assert_true(context.product_page.delete_success)


@when('user searches for a message with search term "{search_term}"')
def step_impl(context, search_term):
    context.product_page.search_for_message(search_term)


@then('the message results are filtered by search term')
def step_impl(context):
    context.product_page.filter_result()
