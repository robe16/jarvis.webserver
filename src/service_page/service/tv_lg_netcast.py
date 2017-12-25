import os
import requests
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail
from log.log import log_outbound


def createPage_tv_lg_netcast(service):
    #
    html_buttons = ''
    html_body = ''
    #
    # Controls
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='6',
                                        service_id=service['service_id'],
                                        function_id='remote',
                                        function_name='Remote',
                                        btn_class='service_function_btn_active')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='remote',
                                     function_body=_html_controls(service),
                                     body_class='service_function_body_active')
    #
    # Apps
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='6',
                                        service_id=service['service_id'],
                                        function_id='apps',
                                        function_name='Apps',
                                        btn_class='')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='apps',
                                     function_body=_html_apps(service),
                                     body_class='')
    #
    args = {'html_buttons': html_buttons,
            'html_body': html_body}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_container.html'), 'r') as f:
        page_body = f.read().format(**args)
    #
    return page_body


def _html_controls(service):
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tv_lg_netcast/controls.html'), 'r') as f:
        html_controls = f.read().format(service_id=service['service_id'])
    #
    return html_controls


def _html_apps(service):
    #
    try:
        #
        json_applist = _get_applist(service)
        #
        html = ''
        #
        for app in json_applist:
            try:
                #
                args = {'service_id': service['service_id'],
                        'auid': json_applist[app]['auid'],
                        'name': json_applist[app]['name']}
                #
                with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tv_lg_netcast/app_button.html'), 'r') as f:
                    html += f.read().format(**args)
                #
            except Exception as e:
                html += ''
            #
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