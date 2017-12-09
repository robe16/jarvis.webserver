from urllib import urlopen
import datetime
from html.page_body import create_page
from resources.global_resources.services import service_variables
from resources.global_resources.variables import projectName
from resources.enGB.service_status import *
from parameters import discovery_service_mia


def create_servicestatus(services):
    #
    html_current = ''
    html_mia = ''
    #
    for s in services.keys():
        #
        type = services[s]['service_type']
        #
        if type in service_variables:
            #
            if service_variables[type]['type']:
                img_type = service_variables[type]['type']
            else:
                img_type = 'logo_other.png'
            #
            if service_variables[type]['logo']:
                img_logo = service_variables[type]['logo']
            else:
                img_logo = 'logo_other.png'
            #
        else:
            img_type = 'logo_other.png'
            img_logo = 'logo_other.png'
        #
        status = 'Online' if services[s]['active'] else 'Offline'
        #
        groups = ''
        for g in services[s]['groups']:
            groups += ', ' if not groups == '' else ''
            groups += g
        #
        args = {'service_id': services[s]['service_id'],
                'service_type': services[s]['service_type'],
                'name_long': services[s]['name_long'],
                'name_short': services[s]['name_short'],
                'status': status,
                'groups': groups,
                'img_type': '/img/service/{img_type}'.format(img_type=img_type),
                'img_logo': '/img/service/{img_logo}'.format(img_logo=img_logo)}
        #
        if services[s]['timestamp'] < (datetime.datetime.now() + datetime.timedelta(seconds=discovery_service_mia)):
            html_current += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
        else:
            html_mia += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
    #
    # Current
    page_body = urlopen('resources/html/service_status/service_header.html').read().encode('utf-8').format(header=service_status_active_header)
    if html_current == '':
        page_body += urlopen('resources/html/service_status/service_null.html').read().encode('utf-8').format(message=service_status_active_none_msg)
    else:
        page_body += '<div class="row">{body}</div>'.format(body=html_current)
    #
    page_body += '<hr>'
    #
    # MIA
    page_body += urlopen('resources/html/service_status/service_header.html').read().encode('utf-8').format(header=service_status_mia_header,
                                                                                                            note=service_status_mia_note)
    if html_mia == '':
        page_body += urlopen('resources/html/service_status/service_null.html').read().encode('utf-8').format(message=service_status_mia_none_msg,
                                                                                                              note=service_status_none_note)
    else:
        page_body += '<div class="row">{body}</div>'.format(body=html_mia)
    #
    return create_page(services,
                       page_body,
                       title=projectName,
                       header=service_status_page_header)
