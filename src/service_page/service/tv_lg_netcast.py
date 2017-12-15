import requests
from urllib import urlopen
from resources.global_resources.variables import *
from log.log import log_outbound


def createPage_tv_lg_netcast(service):
    #
    args = {'service_id': service['service_id'],
            'apps': _html_apps(service)}
    #
    page_body = urlopen('resources/html/services/tv_lg_netcast/tv_lg_netcast.html').read().encode('utf-8').format(**args)
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
        count = 1
        for app in json_applist:
            try:
                #
                html += ('<td class="grid_item" style="width: 20%; cursor: pointer; vertical-align: top;" align="center" onclick="sendHttp(\'/service/command/{service_id}?command=executeApp&auid={auid}\', null, \'POST\', false, true)">' +
                         '<img src="/service/image/{service_id}/appIcon?auid={auid}" style="height:50px;"/>' +
                         '<p style="text-align:center; font-size: 13px;">{name}</p>' +
                         '</td>').format(service_id=service['service_id'],
                                         auid=json_applist[app]['auid'],
                                         name=json_applist[app]['name'])
                #
                if count % 4 == 0:
                    html += '</tr><tr style="height:35px; padding-bottom:2px; padding-top:2px">'
                count += 1
                #
            except Exception as e:
                html += ''
            #
        #
        html += '</tr></table></div>'
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
        log_outbound(True, service['service_id'], service_uri_lgtvnetcast_apps_all, 'GET', r.status_code)
        return r.json()
    else:
        log_outbound(False, service['service_id'], service_uri_lgtvnetcast_apps_all, 'GET', r.status_code)
        return False