from behave import *
from functions.login import *
from functions.basic_functions import *
from functions.bootstrap_functions import *
from configuration.param import *

#############################################################################
############################## GIVEN CONDITIONS #############################
#############################################################################

# @given(u'We have active token')
# def step_impl(context):
#     access_expired_time = send_command(context.client, "uci get nomed.token.access_expires")[:-1]
#     is_active = check_valid_time(access_expired_time)
#     assert is_active

@given(u'List of config files')
def step_impl(context):
    context.list_of_files = context.table
    if not context.list_of_files:
        raise ValueError('Fill the table of filenames!')

@given(u'Path to files "{path}"')
def step_imp(context, path):
    context.path_to_files = path


#############################################################################
############################## WHEN CONDITIONS ##############################
#############################################################################

@when(u'We send "{command}" to eCare')
def step_impl(context, command):
    context.out = send_command(context.client, command)

@when(u'We send files to Bootstrap')
def step_impl(context):
    for row in context.list_of_files:
        path_to_file = upload_files(context.path_to_files, row[0])
        """
        - Pobrac pierwszy z tej listy/rzucic blad jak jest wiecej   !
        """
        # print("Sending")
        # context.out = send_file_to_bootstrap(path_to_file, row[0], sn, row[1], True)
        # print("Assigning")
        # context.out = assign_file_to_device(hardwareID, row[0], sn, row[1])
        context.out = send_and_assign_file_to_device(path_to_file, hardwareID, row[0], sn, row[1], True)
        print("Response after assigning: " + str(context.out))
        print("Files sent to Bootstrap")
        assert context.out

@when(u'We send files to device')
def step_impl(context):
    context.out = send_command(context.client, "nomed-serv-get-config")


#############################################################################
############################## THEN CONDITIONS ##############################
#############################################################################

@then(u'We become server response "{response}"')
def step_impl(context, response):
    idx = context.out.find("Server response")
    resp = context.out[idx+17:idx+20]
    assert resp == response, "Incorrect server response: " + resp

@then(u'We get list of config files')
def step_impl(context):
    for name in context.list_of_files:
        assert context.out.find(name), name + " is missing!"

@then(u'We detach file from device')
def step_impl(context):
    for row in context.list_of_files:
        detach_file_from_device(hardwareID, row[0], sn, row[1])