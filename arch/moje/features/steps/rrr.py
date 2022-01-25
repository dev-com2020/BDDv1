from behave import *
import parse

use_step_matcher("cfparse")


@parse.with_pattern(r"x\s+")
def parse_string(s):
    return s.strip()


register_type(x_=parse_string)


@given('user is on {:x_?}{payment} screen')
def step_payment(context, x_, payment):
    print("Payment type: ")
    print(payment)
