from common_functions.urlencode import url_encode
from resources.global_resources.variables import uri_servicestatus
from discovery.group_services import group_services
from resources.groups.groups_functions import get_group_image


def html_menu(services):
    html = _html_menu_lhs(services)
    html += _html_menu_rhs()
    html += open('/resources/html/common/menu_command_result.html', 'r').read()
    return html


def _html_menu_lhs(services):
    #
    html = ''
    #
    ################
    #
    grouped_services = group_services(services)
    #
    if len(grouped_services) == 0:
        return open('/resources/html/common/menu_lhs.html', 'r').read().format(menu='')
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
                html += open('/resources/html/common/menu_item.html', 'r').read().format(**args)
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
    return open('/resources/html/common/menu_lhs.html', 'r').read().format(menu=html)


def _html_menu_rhs():
    return open('/resources/html/common/menu_rhs.html', 'r').read().format(uri_servicestatus=uri_servicestatus)