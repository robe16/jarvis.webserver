import requests
from resources.global_resources.variables import *
from log.log import log_outbound


def sendCmd_virginmedia_tivo(service, command):
    #
    if command['command'] == 'command':
        cmd = {'command': command['code']}
        service_uri = service_uri_command
    elif command['command'] == 'channel':
        cmd = {'channel': command['channel']}
        service_uri = service_uri_virginmediativo_channel
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
    log_outbound(r.status_code == requests.codes.ok, service['service_id'], service_uri_command, 'GET', r.status_code)
    #
    return r.status_code == requests.codes.ok