import os

def get_env_var(name):
    value = os.environ.get(name, None)
    if not value:
        raise Exception("Environment variable {} not set".format(name))
    return value

def build_headers(api_token):
    auth_token = 'Bearer ' + api_token
    headers = {
        'Authorization': auth_token,
        'Content-Type': 'application/json'
    }
    return headers