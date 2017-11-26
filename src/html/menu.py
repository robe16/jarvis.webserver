from urllib import urlopen
from common_functions.urlencode import url_encode
from resources.global_resources.variables import uri_servicestatus
from resources.global_resources.services import service_variables


def html_menu(services):
    html = _html_menu_lhs(services)
    html += _html_menu_rhs()
    return html


def _html_menu_lhs(services):
    #
    html = ''
    #
    for s in services.keys():
        #
        if type in service_variables:
            img = service_variables[type]['logo']
        else:
            img = 'logo_other.png'
        #
        html += urlopen('resources/html/common/menu_sidebar_item.html').read().encode('utf-8').\
            format(href='/service/page/{info}'.format(info=url_encode(services[s]['service_id'])),
                   id='{info}'.format(info=services[s]['service_id']),
                   cls='',
                   name=services[s]['name'],
                   img='/img/service/{img}'.format(img=img))
    #
    return urlopen('resources/html/common/menu_lhs.html').read().encode('utf-8').format(menu=html)


def _html_menu_rhs():
    return urlopen('resources/html/common/menu_rhs.html').read().encode('utf-8').format(uri_servicestatus=uri_servicestatus)