from behave import given, when, then
from hamcrest import assert_that, has_items
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder


@then('we will have the following people in "{department}"')
def step_impl(context, department):
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
    expected_persons = [row["name"] for row in context.table]
    actual_persons = department_.members

    assert_that(contains_inanyorder(*expected_persons), actual_persons)


@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
    expected_persons = [row["name"] for row in context.table]
    actual_persons = department_.members
    assert_that(has_items(*expected_persons), actual_persons)
