from behave import *

from features.steps.login_module import LModel


@given('Collection of credentials')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = LModel()

    for r in context.table:
        context.model.usr_addition(r["username"], password=r["password"])


@then('user should be logged in')
def step_impl(context):
    pass
