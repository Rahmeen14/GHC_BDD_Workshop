from behave import *

@given('user has created an account on the website')
def step_impl(context):
    pass

@when('they log in to their account')
def step_impl(context):
    assert True is not False

@then('they should be able to view their booking history')
def step_impl(context):
    assert context.failed is False

@then('they should be able to view their upcoming flights')
def step_impl(context):
    assert context.failed is False

@then('they should be able to make changes to their bookings as needed')
def step_impl(context):
    assert context.failed is False

@given('user logged in to their account')
def step_impl(context):
    pass

@when('they navigate to the account settings page')
def step_impl(context):
    assert True is not False

@then('they should be able to update their personal information like contact information')
def step_impl(context):
    assert context.failed is False

@then('they should be able to update their preferences like food, seat etc')
def step_impl(context):
    assert context.failed is False

@given('user is enrolled in the loyalty program')
def step_impl(context):
    pass

@when('they they book a flight')
def step_impl(context):
    assert True is not False

@then('they should earn loyalty points for that booking')
def step_impl(context):
    assert context.failed is False

@then('they should be able to view their balance points')
def step_impl(context):
    assert context.failed is False

@then('they should be able to redeem points for future bookings')
def step_impl(context):
    assert context.failed is False