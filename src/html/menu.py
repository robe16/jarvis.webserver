from urllib import urlopen
from common_functions.urlencode import url_encode
from resources.global_resources.variables import uri_servicestatus
from resources.global_resources.services import service_variables
from discovery.group_services import group_services
from resources.groups.groups_functions import get_group_image


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
                img = get_group_image(g)
                img = img if img else 'logo_other.png'
                #
                args = {'id': g,
                        'class': '',
                        'href': '/group/page/{group_id}'.format(group_id=url_encode(g)),
                        'name': g,
                        'img': '/img/group/{img}'.format(img=img)}
                #
                html += urlopen('resources/html/common/menu_item.html').read().encode('utf-8').format(**args)
                #
                #
            except:
                pass
        #
        if len(grouped_services[c].keys()) > 0:
            html += '<span class="menu_divider btn_shadow"></span>'
    #
    ################
    #
    return urlopen('resources/html/common/menu_lhs.html').read().encode('utf-8').format(menu=html)


def _html_menu_rhs():
    return urlopen('resources/html/common/menu_rhs.html').read().encode('utf-8').format(uri_servicestatus=uri_servicestatus)