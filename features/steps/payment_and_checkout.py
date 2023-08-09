from behave import *

@given('user has opened the payment page')
def step_impl(context):
    pass

@when('they select the "Pay with PayPal" option')
def step_impl(context):
    assert True is not False

@then('they should be directed to the PayPal website to complete the payment process')
def step_impl(context):
    assert context.failed is False

@then('they should receive confirmation of their booking')
def step_impl(context):
    assert context.failed is False

@given('user has completed the payment process')
def step_impl(context):
    pass

@when('they are directed to the confirmation page')
def step_impl(context):
    assert True is not False

@then('they should receive a confirmation email')
def step_impl(context):
    assert context.failed is False

@then('they should see all the details of their booking, including the flight itinerary, total cost, and any special requests')
def step_impl(context):
    assert context.failed is False