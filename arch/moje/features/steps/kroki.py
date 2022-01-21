from behave import *
from product import Product


@given("I created product called {name} with the price {price} and VAT {vat}")
def step_impl(context, name, price, vat):
    context.product = Product(name, float(price), int(vat))


@then("the vat value will be {vat_value}")
def step_impl(context, vat_value):
    assert context.product.vat_value == float(vat_value)