import json
import os

file_name = 'config.json'


def get_config_json():
    #
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as data_file:
        return json.load(data_file)


def get_cfg_serviceid():
    return get_config_json()['service_id']


def get_cfg_port_broadcast():
    return get_config_json()['port']['broadcast']


def get_cfg_port_listener():
    return get_config_json()['port']['listener']