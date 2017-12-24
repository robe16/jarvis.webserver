import os
from common_functions.urlencode import url_encode
from resources.global_resources.variables import uri_servicestatus
from resources.global_resources.logs import logException
from resources.lang.enGB.logs import logDesc_htmlMenu
from log.log import log_internal
from discovery.group_services import group_services
from resources.groups.groups_functions import get_group_image


def html_menu(services):
    html = _html_menu_lhs(services)
    html += _html_menu_rhs()
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_command_result.html'), 'r') as f:
        html += f.read()
    return html


def _html_menu_lhs(services):
    #
    try:
        #
        html = ''
        #
        grouped_services = group_services(services)
        #
        if not bool(grouped_services):
            with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_lhs.html'), 'r') as f:
                return f.read().format(menu='')
        #
        for c, v in grouped_services.items():
            #
            for g, v in grouped_services[c].items():
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
                    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_item.html'), 'r') as f:
                        html += f.read().format(**args)
                    #
                    #
                except Exception as e:
                    log_internal(logException, logDesc_htmlMenu, description=g, exception=e)
                    pass
            #
            if len(grouped_services[c].items()) > 0:
                html += '<span class="menu_divider btn_shadow"></span>'
        #
        with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_lhs.html'), 'r') as f:
            return f.read().format(menu=html)
        #
    except Exception as e:
        log_internal(logException, logDesc_htmlMenu, exception=e)
        with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_lhs.html'), 'r') as f:
            return f.read().format(menu='')


def _html_menu_rhs():
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_rhs.html'), 'r') as f:
        return f.read().format(uri_servicestatus=uri_servicestatus)