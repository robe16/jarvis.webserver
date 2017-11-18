import datetime
from socket import socket, AF_INET, SOCK_DGRAM
from resources.global_resources.variables import jarvis_broadcastPort, service_uri_config
import requests


def discover_services(services):
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('0.0.0.0', jarvis_broadcastPort))
    #:
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        if data.startswith('jarvis'):
            data = data.split('::')
            #
            url = 'http://{ip}:{port}{uri}'.format(ip=addr[0],
                                                   port=data[3],
                                                   uri=service_uri_config)
            r = requests.get(url)
            #
            if r.status_code == requests.codes.ok:
                r = r.json()
                service_name = r['name']
                service_groups = r['groups']
            else:
                service_name = ''
                service_groups = []
            #
            services[str(data[1])] = {'service_id': str(data[1]),
                                      'service_type': str(data[2]),
                                      'name': service_name,
                                      'groups': service_groups,
                                      'ip': addr[0],
                                      'port': str(data[3]),
                                      'active': True,
                                      'timestamp': datetime.datetime.now()}
