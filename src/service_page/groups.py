from urllib.request import urlopen
from common_functions.urlencode import url_decode
from resources.lang.enGB.logs import *
from resources.global_resources.variables import projectName
from resources.global_resources.services import service_variables
from resources.global_resources.logs import logPass, logException
from resources.groups.groups_functions import get_group_category
from discovery.group_services import group_services
from service_page.services import serviceHtml
from html.page_body import create_page
from log.log import log_internal


def groupPage(services, group_id):
    #
    resources = '<script src="/resource/js/jarvis.service_page.js"></script>'
    resources += '<script src="/resource/js/jarvis.service_group.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_page.css">'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_group.css">'
    #
    return create_page(services,
                       groupHtml(services, group_id),
                       resources=resources,
                       title='{projectName}: {name}'.format(projectName=projectName,
                                                            name=url_decode(group_id)),
                       header=url_decode(group_id))


def groupHtml(services, group_id):
    #
    grouped_services = group_services(services)
    #
    group_name = url_decode(group_id)
    category = get_group_category(group_name)
    #
    try:
        #
        first_item = True
        #
        html_buttons = ''
        html_pages = ''
        #
        for service in grouped_services[category][group_name]['services']:
            #
            type = services[service]['service_type']
            if type in service_variables:
                img = service_variables[type]['type']
            else:
                img = 'logo_other.png'
            #
            if first_item:
                class_buttons = ''
                class_page = 'grp_body_show'
                first_item = False
            else:
                class_buttons = 'btn_shadow grayscale'
                class_page = 'grp_body_hide'
            #
            args = {'service_id': services[service]['service_id'],
                    'img': '/img/service/{img}'.format(img=img),
                    'name': services[service]['name_long'],
                    'class': class_buttons}
            #
            html_buttons += urlopen('resources/html/groups/group_item_btn.html').read().encode('utf-8').format(**args)
            #
            args = {'service_id': services[service]['service_id'],
                    'service_body': serviceHtml(services, services[service]['service_id']),
                    'class': class_page}
            #
            html_pages += urlopen('resources/html/groups/group_item_body.html').read().encode('utf-8').format(**args)
            #
        #
        for subservice in grouped_services[category][group_name]['subservices']:
            pass
            #
            # TODO
        #
        args = {'service_buttons': html_buttons,
                'service_pages': html_pages}
        #
        log_internal(logPass, logDesc_groupPage, description=group_id)
        #
        return urlopen('resources/html/groups/group.html').read().encode('utf-8').format(**args)
        #
    except Exception as e:
        #
        log_internal(logException, logDesc_groupPage, description=group_id, exception=e)
        #
        return urlopen('resources/html/groups/group_error.html').read().encode('utf-8').format(group_id=group_id)
