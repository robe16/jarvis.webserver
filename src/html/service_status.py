import datetime
from urllib import urlopen

from common_functions.urlencode import url_encode
from html.page_body import create_page
from parameters import discovery_service_mia
from resources.global_resources.services import service_variables
from resources.global_resources.variables import projectName
from resources.groups.groups_functions import get_group_image
from resources.lang.enGB.service_status import *


def create_servicestatus(services):
    #
    resources = '<script src="/resource/js/jarvis.service_status.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_status.css">'
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
        if len(services[s]['groups']) > 0:
            html_groups = ''
            for g in services[s]['groups']:
                g_args = {'group_name': g,
                          'href': '/group/page/{group_id}'.format(group_id=url_encode(g)),
                          'img_filename': get_group_image(g)}
                html_groups += urlopen('resources/html/service_status/service_group_img.html').read().encode('utf-8').format(**g_args)
        else:
            html_groups = '<p>n/a</p>'
        #
        args = {'service_id': services[s]['service_id'],
                'service_type': services[s]['service_type'],
                'name_long': services[s]['name_long'],
                'name_short': services[s]['name_short'],
                'groups': html_groups,
                'subservices': _html_subservices(services[s]['subservices']),
                'status': status,
                'img_type': '/img/service/{img_type}'.format(img_type=img_type),
                'img_logo': '/img/service/{img_logo}'.format(img_logo=img_logo)}
        #
        if services[s]['timestamp'] < (datetime.datetime.now() + datetime.timedelta(seconds=discovery_service_mia)):
            html_current += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
        else:
            html_mia += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
    #
    # Current
    page_body = urlopen('resources/html/service_status/service_header.html').read().encode('utf-8').format(header=service_status_active_header,
                                                                                                           note=service_status_active_note)
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
        page_body += urlopen('resources/html/service_status/service_null.html').read().encode('utf-8').format(message=service_status_mia_none_msg)
    else:
        page_body += '<div class="row">{body}</div>'.format(body=html_mia)
    #
    return create_page(services,
                       page_body,
                       resources=resources,
                       title=projectName,
                       header=service_status_page_header)


def _html_subservices(subservices):
    #
    if len(subservices) > 0:
        html_subservices = ''
        #
        for sub in subservices:
            #
            if len(sub['groups']) > 0:
                html_groups = ''
                for g in sub['groups']:
                    g_args = {'group_name': g,
                              'img_filename': get_group_image(g)}
                    html_groups += urlopen('resources/html/service_status/service_group_img.html').read().encode('utf-8').format(**g_args)
            else:
                html_groups = '<p>n/a</p>'
            #
            args = {'subservice_id': sub['id'],
                    'subservice_type': sub['type'],
                    'subservice_groups': html_groups}
            #
            html_subservices += urlopen('resources/html/service_status/subservice_item.html').read().encode('utf-8').format(**args)
        #
    else:
        html_subservices = '<div class="row"><p>n/a</p></div>'
    #
    return '<div class="container-fluid">{body}</div>'.format(body=html_subservices)