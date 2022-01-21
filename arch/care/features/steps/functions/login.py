import sys
import paramiko
from steps.configuration.param import *




def login(client):
    try:
        keyfile = paramiko.RSAKey.from_private_key_file(keyfile_path, password=password)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # dlaczego to jest? Jakby tego nie było to co by się stało?
        print("Connecting to device")
        client.connect(hostname=hostname, username=username, password=password, pkey=keyfile)
        print("Connected")
    except Exception as ex:
        print("Login failed")
        print(str(ex))
        sys.exit(1)

def logout(client):
    print("Logging out")
    client.close()
    