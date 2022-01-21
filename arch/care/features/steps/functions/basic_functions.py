import time

def is_token_active(client):
    access_expired_time = send_command(client, "uci get nomed.token.access_expires")[:-1]
    is_active = check_valid_time(access_expired_time)
    return is_active

def send_command(client, command):
    input, output, errors = client.exec_command(command)
    e = errors.read().decode()
    if(e):
        print(e)
    out = output.read().decode()
    return out

def check_valid_time(recieved_time):
    if(int(recieved_time) > time.time()):
        return True
    else:
        return False
