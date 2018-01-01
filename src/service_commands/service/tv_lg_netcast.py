import requests
from log.log import log_outbound
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail


def sendCmd_tv_lg_netcast(service, command):
    #
    if command['command'] == 'keyInput':
        cmd = {'keyInput': command['key']}
        service_uri = service_uri_lgtvnetcast_command_keyInput
    elif command['command'] == 'executeApp':
        cmd = {'executeApp': command['auid']}
        service_uri = service_uri_lgtvnetcast_command_executeApp
    elif command['command'] == 'cursorVisbility':
        cmd = {'visibility': command['visibility']}
        service_uri = service_uri_lgtvnetcast_command_cursorVisbility
    elif command['command'] == 'touchMove':
        cmd = {'touchMoveX': command['touchMoveX'],
               'touchMoveY': command['touchMoveY']}
        service_uri = service_uri_lgtvnetcast_command_touchMove
    elif command['command'] == 'touchClick':
        cmd = {}
        service_uri = service_uri_lgtvnetcast_command_touchClick
    elif command['command'] == 'touchWheel':
        cmd = {'touchWheelDirection': command['touchWheelDirection']}
        service_uri = service_uri_lgtvnetcast_command_touchWheel
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
    #
    logResult = logPass if (r.status_code == requests.codes.ok) else logFail
    log_outbound(logResult,
                 service['ip'], service['port'], 'POST', service_uri_command,
                 '-', cmd,
                 r.status_code)
    #
    return r.status_code == requests.codes.ok
