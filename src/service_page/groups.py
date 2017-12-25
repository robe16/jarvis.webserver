import os
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
    resources += '<script src="/resource/js/jarvis.service_functions.js"></script>'
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
        if bool(grouped_services):
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
                with open(os.path.join(os.path.dirname(__file__), '../resources/html/groups/group_item_btn.html'), 'r') as f:
                    html_buttons += f.read().format(**args)
                #
                args = {'service_id': services[service]['service_id'],
                        'service_body': serviceHtml(services, services[service]['service_id']),
                        'class': class_page}
                #
                with open(os.path.join(os.path.dirname(__file__), '../resources/html/groups/group_item_body.html'), 'r') as f:
                    html_pages += f.read().format(**args)
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
        with open(os.path.join(os.path.dirname(__file__), '../resources/html/groups/group.html'), 'r') as f:
            return f.read().format(**args)
        #
    except Exception as e:
        #
        log_internal(logException, logDesc_groupPage, description=group_id, exception=e)
        #
        with open(os.path.join(os.path.dirname(__file__), '../resources/html/groups/group_error.html'), 'r') as f:
            return f.read().format(group_id=group_id)
