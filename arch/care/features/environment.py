from behave import *
from paramiko import *
from steps.functions.basic_functions import *
from steps.functions.login import *
from steps.functions.bootstrap_functions import detach_file_from_device
from steps.configuration.param import *

def before_all(context):
    context.client = paramiko.SSHClient()
    login(context.client)
    print("Before all")

def before_scenario(context, scenario):
    # access_expired_time = is_token_active(context.client)
    assert context.client != None, "Connection with device is lost"
    # and access_expired_time

"""
def after_feature(context, feature):
    print(context.out)
    for row in context.list_of_files:
        detach_file_from_device(hardwareID, row[0], sn, row[1])
"""
    
def after_all(context):
    logout(context.client)