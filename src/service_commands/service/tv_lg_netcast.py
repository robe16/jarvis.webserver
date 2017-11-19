import requests
from resources.global_resources.variables import *


def sendCmd_tv_lg_netcast(service, command):
    #
    if command['command'] == 'keyInput':
        key = command['key']
        auid = ''
        name = ''
    elif command['command'] == 'executeApp':
        key = ''
        auid = command['auid']
        name = command['name']
    else:
        return False
    #
    cmd = {'command': command['command'],
           'keyInput': {'key': key},
           'executeApp': {'auid': auid,
                          'name': name}}
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_command)
    #
    r = requests.post(service_url, json=cmd)
    print(r.url)
    #
    return r.status_code == requests.codes.ok
