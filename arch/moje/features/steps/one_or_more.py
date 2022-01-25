#------------------------------
# Model
#------------------------------
class Meeting():
    def __init__(self):
        self.persons = set()

from behave import register_type
from parse_type import TypeBuilder

company_persons = ["Alice", "Bob", "Charly", "Dodo"]
parse_person = TypeBuilder.make_choice(company_persons)
register_type(Person=parse_person)

parse_persons = TypeBuilder.with_many(parse_person, listsep="and")
register_type(PersonAndMore=parse_persons)

#------------------------------
# Kroki
#------------------------------

from behave import given, when, then

@when('I meet {persons:Person+}')
def step_when_I_meet_persons(context, persons):
    for person in persons:
        context.meeting.persons.add(person)

@when('I meet {persons:PersonAndMore}')
def step_when_I_meet_person_and_more(context, persons):
    for person in persons:
        context.meeting.persons.add(person)


#------------------------------
# Dalsze kroki
#------------------------------
from hamcrest import assert_that, contains_exactly

@given('I go to a meeting')
def step_given_I_go_to_meeting(context):
    context.meeting = Meeting()

@then('the following persons are present')
def step_following_persons_are_present(context):
    assert context.table, "table<Person> is required"
    actual_persons = sorted(context.meeting.persons)
    expected_persons = [row["name"] for row in context.table]

    assert_that(actual_persons, contains_exactly(*expected_persons))


