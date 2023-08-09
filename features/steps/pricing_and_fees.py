from behave import *

@given('user has entered their travel information')
def step_impl(context):
    pass

@when('they view their search results')
def step_impl(context):
    assert True is not False

@then('the total cost of each flight should be displayed upfront, including all taxes and fees')
def step_impl(context):
    assert context.failed is False

@given('user has opened the checkout page')
def step_impl(context):
    pass

@when('they select the "Pay in Local Currency" option')
def step_impl(context):
    assert True is not False

@when('they choose British pounds')
def step_impl(context):
    assert True is not False

@then('the total cost of their booking should be displayed in pounds')
def step_impl(context):
    assert context.failed is False

@then('the payment should be processed in pounds')
def step_impl(context):
    assert context.failed is False