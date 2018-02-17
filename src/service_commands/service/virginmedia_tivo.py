import requests
from log.log import log_outbound
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail


def sendCmd_virginmedia_tivo(service, command):
    #
    if command['command'] == 'command':
        cmd = {'command': command['code']}
        service_uri = service_uri_command
    elif command['command'] == 'channel':
        cmd = {'channel': command['channel']}
        service_uri = service_uri_virginmediativo_channel
    elif command['command'] == 'enterpin':
        cmd = {}
        service_uri = service_uri_virginmediativo_enterpin
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