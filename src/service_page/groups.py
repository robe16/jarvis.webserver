from urllib import urlopen
from common_functions.urlencode import url_encode, url_decode
from resources.global_resources.services import service_variables
from resources.groups.groups_functions import get_group_category, get_group_image
from discovery.group_services import group_services
from services import serviceHtml

def groupPage(services, group_id):
    #
    grouped_services = group_services(services)
    #
    group_name = url_decode(group_id)
    category = get_group_category(group_name)
    #
    try:
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
            args = {'href': '#',
                    'img': img,
                    'name': services[service]['name_long']}
            #
            html_buttons += urlopen('resources/html/services/group_service_img.html').read().encode('utf-8').format(**args)
            #
            html_pages += serviceHtml(services, services[service]['service_id'])
            #
        #
        for subservice in grouped_services[category][group_name]['subservices']:
            #
            # TODO
            pass
            #
            # type = services[subservice['service_id']]['service_type']
            # if type in service_variables:
            #     img = service_variables[type]['type']
            # else:
            #     img = 'logo_other.png'
            # #
            # args = {'id': subservice['service_id'],
            #         'class': 'menu_item_service',
            #         'href': '/service/page/{service_id}?group={group}'.format(service_id=subservice['service_id'],
            #                                                                   group=url_encode(g)),
            #         'name': services[subservice['service_id']]['name_long'],
            #         'img': '/img/service/{img}'.format(img=img)}
            # #
            # html_group += urlopen('resources/html/common/menu_item.html').read().encode('utf-8').format(**args)
        #
        args = {'service_buttons': html_buttons,
                'service_pages': html_pages}
        #
        return urlopen('resources/html/services/group.html').read().encode('utf-8').format(**args)
        #
        #
    except:
        pass
    #
    return ''
