import requests
from resources.global_resources.variables import *


def getImage_tv_lg_netcast(service, filename, query):
    #
    if filename == 'appIcon':
        return _getImage(service, query['auid'], query['name'])
    else:
        return False


def _getImage(service, auid, name):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_lgtvnetcast_image.format(auid=auid,
                                                                                            name=name))
    #
    r = requests.get(service_url)
    #
    if r.status_code == requests.codes.ok:
        return r.content
    else:
        # log_error('LG TV - Attempted to request {data} from server - {status}'.format(data=datarequest, status=r.status_code))
        return False