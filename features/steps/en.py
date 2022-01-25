from parse_type import TypeBuilder
from behave import register_type
from behave import when, then
from hamcrest import assert_that, equal_to

answer_oracle = {
    "Do you love me?": True,
    "Do you hate me?": False,
    "Do you kiss me?": True,
}


parse_yesno = TypeBuilder.make_enum({"yes": True, "no": False, "silence": True})
register_type(YesNo=parse_yesno)

@when(u'Romeo asks Julia: "{question}"')
def step_when_romeo_asks_julia(context, question):
    context.question = question

@then(u'the answer is "{answer:YesNo}"')
def step_then_the_answer_is(context, answer):
    assert_that(answer, equal_to(answer_oracle.get(context.question, None)))
