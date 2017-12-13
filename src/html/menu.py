from urllib import urlopen
from common_functions.urlencode import url_encode
from resources.global_resources.variables import uri_servicestatus
from resources.global_resources.services import service_variables
from discovery.group_services import group_services
from resources.groups.groups_functions import get_group_category_list, get_group_image


def html_menu(services):
    html = _html_menu_lhs(services)
    html += _html_menu_rhs()
    html += urlopen('resources/html/common/menu_command_result.html').read().encode('utf-8')
    return html


def _html_menu_lhs(services):
    #
    html = ''
    #
    ################
    #
    grouped_services = group_services(services)
    #
    for c in grouped_services.keys():
        #
        for g in grouped_services[c].keys():
            #
            try:
                #
                html_group = ''
                #
                for service in grouped_services[c][g]['services']:
                    #
                    type = services[service]['service_type']
                    if type in service_variables:
                        img = service_variables[type]['type']
                    else:
                        img = 'logo_other.png'
                    #
                    args = {'id': service,
                            'class': 'menu_item_service',
                            'href': '/service/page/{service_id}'.format(service_id=service),
                            'name': services[service]['name_long'],
                            'img': '/img/service/{img}'.format(img=img)}
                    #
                    html_group += urlopen('resources/html/common/menu_item_service.html').read().encode('utf-8').format(**args)
                #
                for subservice in grouped_services[c][g]['subservices']:
                    #
                    type = services[subservice['service_id']]['service_type']
                    if type in service_variables:
                        img = service_variables[type]['type']
                    else:
                        img = 'logo_other.png'
                    #
                    args = {'id': subservice['service_id'],
                            'class': 'menu_item_service',
                            'href': '/service/page/{service_id}?group={group}'.format(service_id=subservice['service_id'],
                                                                                      group=url_encode(g)),
                            'name': services[subservice['service_id']]['name_long'],
                            'img': '/img/service/{img}'.format(img=img)}
                    #
                    html_group += urlopen('resources/html/common/menu_item_service.html').read().encode('utf-8').format(**args)
                #
                img = get_group_image(g)
                img = img if img else 'logo_other.png'
                #
                args = {'group_id': '{info}'.format(info=url_encode(g)),
                        'group_name': g,
                        'group_img': '/img/group/{img}'.format(img=img),
                        'html_group_items': html_group}
                #
                html += urlopen('resources/html/common/menu_item_group.html').read().encode('utf-8').format(**args)
                #
                #
            except:
                pass
        #
        if len(grouped_services[c].keys()) > 0:
            html += '<span class="menu_divider shadow"></span>'
    #
    ################
    #
    for s in services.keys():
        #
        type = services[s]['service_type']
        if type in service_variables:
            img = service_variables[type]['type']
        else:
            img = 'logo_other.png'
        #
        args = {'id': '{info}'.format(info=services[s]['service_id']),
                'class': '',
                'href': '/service/page/{service_id}'.format(service_id=url_encode(services[s]['service_id'])),
                'name': services[s]['name_long'],
                'img': '/img/service/{img}'.format(img=img)}
        #
        html += urlopen('resources/html/common/menu_item_service.html').read().encode('utf-8').format(**args)
    #
    return urlopen('resources/html/common/menu_lhs.html').read().encode('utf-8').format(menu=html)


def _html_menu_rhs():
    return urlopen('resources/html/common/menu_rhs.html').read().encode('utf-8').format(uri_servicestatus=uri_servicestatus)