import os
import requests
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail, logException
from log.log import log_outbound


def createPage_xbox_one(service):
    #
    resources = '<link rel="stylesheet" href="/resource/css/jarvis.service_page.xbox_one.css">'
    #
    html_buttons = ''
    html_body = ''
    #
    # Controls
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='12',
                                        service_id=service['service_id'],
                                        function_id='controls',
                                        function_name='Controls',
                                        btn_class='service_function_btn_active')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='controls',
                                     function_body=_html_controls(service),
                                     body_class='service_function_body_active')
    #
    args = {'service_id': service['service_id'],
            'resources': resources,
            'html_buttons': html_buttons,
            'html_body': html_body}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_container.html'), 'r') as f:
        page_body = f.read().format(**args)
    #
    return page_body


def _html_controls(service):
    #
    try:
        powerStatus = _get_powerstatus(service)
        if powerStatus:
            powerStatus_msg = 'On'
        else:
            powerStatus_msg = 'Off'
    except Exception as e:
        powerStatus_msg = 'Unavailable'
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/xbox_one/controls.html'), 'r') as f:
        html_controls = f.read().format(service_id=service['service_id'],
                                        powerStatus=powerStatus_msg)
    #
    return html_controls


def _get_powerstatus(service):
    #
    try:
        #
        service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                       port=service['port'],
                                                       uri=service_uri_xboxone_powerstatus)
        #
        headers = {service_header_clientid_label: serviceId}
        r = requests.get(service_url, headers=headers)
        #
        if r.status_code == requests.codes.ok:
            log_outbound(logPass,
                         service['ip'], service['port'], 'GET', service_uri_xboxone_powerstatus,
                         '-', '-',
                         r.status_code)
            return r.json()['isOn']
        else:
            log_outbound(logFail,
                         service['ip'], service['port'], 'GET', service_uri_xboxone_powerstatus,
                         '-', '-',
                         r.status_code)
            raise Exception('Could not get power status from service')
    except Exception as e:
        log_outbound(logException,
                     service['ip'], service['port'], 'GET', service_uri_xboxone_powerstatus,
                     '-', '-', '-',
                     exception=e)
        raise Exception('Could not get power status from service')
