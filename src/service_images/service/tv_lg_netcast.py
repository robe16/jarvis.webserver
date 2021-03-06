import requests
from log.log import log_outbound
from resources.global_resources.variables import *
from resources.global_resources.log_vars import logPass, logFail


def getImage_tv_lg_netcast(service, filename, query):
    #
    if filename == 'appIcon':
        return _getImage(service, query['auid'])
    #
    if filename == 'screenshot':
        return _getScreenshot(service)
    else:
        return False


def _getImage(service, auid):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_lgtvnetcast_image_app.format(auid=auid))
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get(service_url, headers=headers)
    #
    if r.status_code == requests.codes.ok:
        log_outbound(logPass,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_image_app.format(auid=auid),
                     '-', '-',
                     r.status_code)
        return r.content
    else:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_image_app.format(auid=auid),
                     '-', '-',
                     r.status_code)
        return False


def _getScreenshot(service):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_lgtvnetcast_image_screenshot)
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get(service_url, headers=headers)
    #
    if r.status_code == requests.codes.ok:
        log_outbound(logPass,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_image_screenshot,
                     '-', '-',
                     r.status_code)
        return r.content
    else:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_image_screenshot,
                     '-', '-',
                     r.status_code)
        return False