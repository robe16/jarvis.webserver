import datetime
from socket import socket, AF_INET, SOCK_DGRAM

import requests

from log.log import log_outbound, log_internal
from resources.global_resources.broadcast import jarvis_broadcastPort
from resources.global_resources.variables import service_uri_config
from resources.lang.enGB.logs import logDesc_services_Discovery


def discover_services(services):
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('0.0.0.0', jarvis_broadcastPort))
        #:
        while True:
            data, addr = s.recvfrom(1024)
            data = data.decode("utf-8")
            if data.startswith('jarvis::discovery'):
                data = data.split('::')
                #
                ip = addr[0]
                service_id = str(data[2])
                service_type = str(data[3])
                port = str(data[4])
                #
                if not service_id in services.keys():
                    #
                    host = 'http://{ip}:{port}'.format(ip=ip, port=port)
                    uri = service_uri_config
                    #
                    r = requests.get('{host}{uri}'.format(host=host, uri=uri))
                    #
                    log_outbound((r.status_code == requests.codes.ok), service_id, uri, 'GET', r.status_code)
                    #
                    if r.status_code == requests.codes.ok:
                        r = r.json()
                        name_long = r['name_long']
                        name_short = r['name_short']
                        service_groups = r['groups']
                        subservices = r['subservices']
                    else:
                        name_long = ''
                        name_short = ''
                        service_groups = []
                        subservices = []
                else:
                    name_long = services[service_id]['name_long']
                    name_short = services[service_id]['name_short']
                    service_groups = services[service_id]['groups']
                    subservices = services[service_id]['subservices']
                #
                services[service_id] = {'service_id': service_id,
                                        'service_type': service_type,
                                        'name_long': name_long,
                                        'name_short': name_short,
                                        'groups': service_groups,
                                        'subservices': subservices,
                                        'ip': ip,
                                        'port': port,
                                        'active': True,
                                        'timestamp': datetime.datetime.now()}
    except Exception as e:
        log_internal(True, logDesc_services_Discovery, desc='fail', exception=e)
