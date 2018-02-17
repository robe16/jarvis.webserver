import requests
from log.log import log_outbound
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail


def sendCmd_nest(service, command):
    #
    cmd = {}
    #
    if command['device_type'] == 'thermostat':
        #
        try:
            cmd['target_temperature_c'] = float(command['target_temperature_c'])
        except:
            pass
        #
        try:
            cmd['target_temperature_f'] = int(command['target_temperature_f'])
        except:
            pass
        #
        service_uri = service_uri_nest_data_device_specific.format(device_type=command['device_type'],
                                                                   device_id=command['device_id'])
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
                 service['ip'], service['port'], 'POST', service_uri,
                 '-', cmd,
                 r.status_code)
    #
    return r.status_code == requests.codes.ok
