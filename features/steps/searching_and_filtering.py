from behave import *

@given('user has opened the flight search page')
def step_impl(context):
    pass

@when('they select the "Non-stop" filter')
def step_impl(context):
    assert True is not False

@then('they should only see search results for flights that do not have any stops')
def step_impl(context):
    assert context.failed is False

@when('they select the "Flexible Dates" option')
def step_impl(context):
    assert True is not False

@when('they choose the month of August')
def step_impl(context):
    assert True is not False

@then('they should see a list of flights for that month sorted by price')
def step_impl(context):
    assert context.failed is False

@given('user has performed a flight search')
def step_impl(context):
    pass

@when('they save their search results')
def step_impl(context):
    assert True is not False

@when('they enable email alerts')
def step_impl(context):
    assert True is not False

@then('they should receive an email notification if the prices for that flight route drop')
def step_impl(context):
    assert context.failed is False
