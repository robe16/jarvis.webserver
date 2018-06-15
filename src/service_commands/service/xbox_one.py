import requests
from log.log import log_outbound
from resources.global_resources.variables import *
from resources.global_resources.log_vars import logPass, logFail


def sendCmd_xbox_one(service, command):
    #
    if command['command'] == 'power':
        cmd = {'command': 'power'}
        service_uri = service_uri_command
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
    logResult = logPass if (r.status_code == requests.codes.ok) else logFail
    log_outbound(logResult,
                 service['ip'], service['port'], 'POST', service_uri,
                 '-', cmd,
                 r.status_code)
    #
    return r.status_code == requests.codes.ok