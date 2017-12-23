import os
import requests
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail
from log.log import log_outbound


def createPage_tv_lg_netcast(service):
    #
    args = {'service_id': service['service_id'],
            'apps': _html_apps(service)}
    #
    page_body = open(os.path.join(os.path.dirname(__file__), '../resources/html/services/tv_lg_netcast/tv_lg_netcast.html'), 'r').read().format(**args)
    #
    return page_body


def _html_apps(service):
    #
    try:
        #
        json_applist = _get_applist(service)
        #
        html = '<table style="width:100%">' +\
               '<tr style="height:80px; padding-bottom:2px; padding-top:2px">'
        #
        count = 0
        for app in json_applist:
            try:
                #
                if not count == 0 and count % 4 == 0:
                    html += '</tr><tr style="height:35px; padding-bottom:2px; padding-top:2px">'
                #
                args = {'service_id': service['service_id'],
                        'auid': json_applist[app]['auid'],
                        'name': json_applist[app]['name']}
                #
                html += open(os.path.join(os.path.dirname(__file__), '../resources/html/services/tv_lg_netcast/app_button.html'), 'r').read().format(**args)
                #
                count += 1
                #
            except Exception as e:
                html += ''
        #
        html += '</tr></table>'
        return html
    except:
        return '<p style="text-align:center">App list could has not been retrieved from the device.</p>' +\
               '<p style="text-align:center">Please check the TV is turned on and then try again.</p>'


def _get_applist(service):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_lgtvnetcast_apps_all)
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get(service_url, headers=headers)
    #
    if r.status_code == requests.codes.ok:
        log_outbound(logPass,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_apps_all,
                     '-', '-',
                     r.status_code)
        return r.json()
    else:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_apps_all,
                     '-', '-',
                     r.status_code)
        return False