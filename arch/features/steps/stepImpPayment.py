from behave import *
from runner import *

@given('User is on Payment screen')
def impl_bkpy(context):
    context.payment = Payment()
    print('User is on Payment screen')


@when('User clicks on Payment types')
def impl_bkpy(context):
    context.payment.card()
    print('User clicks on Payment types')


@then('User should get Cash')
def impl_bkpy(context):
    print('User should get Cash')
    assert (context.payment.type == ['cash'])
