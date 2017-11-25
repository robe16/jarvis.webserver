import requests
from log.log import Log
from resources.global_resources.variables import *


_log = Log()


def getImage_tv_lg_netcast(service, filename, query):
    #
    if filename == 'appIcon':
        return _getImage(service, query['auid'])
    else:
        return False


def _getImage(service, auid):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_lgtvnetcast_image.format(auid=auid))
    #
    r = requests.get(service_url)
    #
    if r.status_code == requests.codes.ok:
        _log.new_entry(logCategoryProcess, service_url, 'Get app image', 'GET', r.status_code, level=logLevelInfo)
        return r.content
    else:
        _log.new_entry(logCategoryProcess, service_url, 'Get app image', 'GET', r.status_code, level=logLevelError)
        return False