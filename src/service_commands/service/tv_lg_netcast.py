import requests
from resources.global_resources.variables import *
from log.log import log_outbound


def sendCmd_tv_lg_netcast(service, command):
    #
    if command['command'] == 'keyInput':
        cmd = {'keyInput': command['key']}
        service_uri = service_uri_lgtvnetcast_command_keyInput
    elif command['command'] == 'executeApp':
        cmd = {'executeApp': command['auid']}
        service_uri = service_uri_lgtvnetcast_command_executeApp
    else:
        return False
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri)
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.post(service_url, json=cmd, headers=headers)
    #
    log_outbound(r.status_code == requests.codes.ok, '{ip}:{port}'.format(ip=service['ip'], port=service['port']),
                 service_uri_command, 'GET', r.status_code)
    #
    return r.status_code == requests.codes.ok
