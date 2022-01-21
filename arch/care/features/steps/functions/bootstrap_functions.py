# Copyright (C) Comarch SA. All rights reserved.

import requests
import json
from filecmp import cmp
from steps.configuration.param import *
from Crypto.Cipher import AES

BASE_URL = "https://srfxfz.comarch-iot.com"
BOOTSTRAP_TOKEN = "rGMcX9mtrWpiozbsSnamc6IcPk8YChQV"

def print_http_error(response):
    if response.status_code != 200:
        detail = ""
        try:
            detail = json.loads(response.text)['detail']
        except:
            pass
        print("Response code: " + str(response.status_code) + " " + detail)

def send_file_to_bootstrap(filepath, file_type, variant, version, encrypted):
    files = {'file' : open(filepath, 'rb')}
    if version == None:
        url = "{}/bootstrap/api/files?type={}&variant={}&encrypted={}".format(BASE_URL, file_type, variant, encrypted)
    else:
        url = "{}/bootstrap/api/files?type={}&variant={}&version={}&encrypted={}".format(BASE_URL, file_type, variant, version, encrypted)
    headers = {'Private-token': BOOTSTRAP_TOKEN, 'Accept': '*/*'}
    response = requests.post(url, files = files, headers = headers)
    print_http_error(response)
    return response.status_code == 200 or response.status_code == 409

def assign_file_to_device(hardwareID, file_type, variant, version):
    if version is None:
        version = '_newest'
    url = "{}/bootstrap/api/bootstrap/{}/configs/{}?variant={}&version={}".format(BASE_URL, hardwareID, file_type, variant, version)
    headers = {'Private-token': BOOTSTRAP_TOKEN, 'Accept': '*/*', 'Content-Type': 'application/json'}
    response = requests.post(url, headers = headers)
    print_http_error(response)
    return response.status_code == 200 or response.status_code == 409

def detach_file_from_device(hardwareID, file_type, variant, version):
    if version == None:
        url = "{}/bootstrap/api/bootstrap/{}/configs/{}?variant={}".format(BASE_URL, hardwareID, file_type, variant)
    else:
        url = "{}/bootstrap/api/bootstrap/{}/configs/{}?variant={}&version={}}".format(BASE_URL, hardwareID, file_type, variant, version)
    headers = {'Private-token': BOOTSTRAP_TOKEN, 'Accept': '*/*'}
    response = requests.delete(url, headers = headers)
    print_http_error(response)
    return response.status_code == 200

def send_and_assign_file_to_device(filepath, hardwareID, file_type, variant, version, encrypted):
    if not send_file_to_bootstrap(filepath, file_type, variant, version, encrypted):
        return False
    if not assign_file_to_device(hardwareID, file_type, variant, version):
        return False
    return True

def compare_uploaded_files(file_from_bootstrap, file_from_computer):
    assert(cmp(file_from_bootstrap, file_from_computer))