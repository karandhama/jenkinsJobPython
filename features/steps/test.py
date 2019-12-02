from behave import *

@given("a dealer")
def step_impl(context):
    dealer_name = "karan"

@when("the round starts")
def step_impl(context):
    start = 0

@then("the dealer gives itself two cards")
def step_impl(context):
    card = 2
    assert card==2, "Number of cards are not two"