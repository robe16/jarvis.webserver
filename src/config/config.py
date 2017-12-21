import json
import os
import ast
import datetime
from resources.global_resources.variables import oauthConfigTimeformat

file_name = 'config.json'


def get_config_json():
    #
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as data_file:
        return json.load(data_file)


def get_cfg_port_broadcast():
    return get_config_json()['port']['broadcast']


def get_cfg_port_listener():
    return get_config_json()['port']['listener']