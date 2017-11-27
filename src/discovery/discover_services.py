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
                url = 'http://{ip}:{port}{uri}'.format(ip=ip,
                                                       port=port,
                                                       uri=service_uri_config)
                r = requests.get(url)
                #
                if r.status_code == requests.codes.ok:
                    r = r.json()
                    name_long = r['name_long']
                    name_short = r['name_short']
                    service_groups = r['groups']
                else:
                    name_long = ''
                    name_short = ''
                    service_groups = []
            else:
                name_long = services[service_id]['name_long']
                name_short = services[service_id]['name_short']
                service_groups = services[service_id]['groups']
            #
            services[service_id] = {'service_id': service_id,
                                    'service_type': service_type,
                                    'name_long': name_long,
                                    'name_short': name_short,
                                    'groups': service_groups,
                                    'ip': ip,
                                    'port': port,
                                    'active': True,
                                    'timestamp': datetime.datetime.now()}
