import datetime
from socket import socket, AF_INET, SOCK_DGRAM
from resources.global_resources.variables import jarvis_broadcastPort


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
            services[str(data[1])] = {'service_id': str(data[1]),
                                      'service_type': str(data[2]),
                                      'ip': addr[0],
                                      'port': str(data[3]),
                                      'active': True,
                                      'timestamp': datetime.datetime.now()}
