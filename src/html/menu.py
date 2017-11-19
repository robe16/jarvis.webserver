from urllib import urlopen
from resources.global_resources.variables import uri_servicestatus


def html_menu(services):
    html = _html_menu_lhs()
    html += _html_menu_rhs()
    return html


def _html_menu_lhs():
    return urlopen('resources/html/common/menu_lhs.html').read().encode('utf-8').format(menu='')


def _html_menu_rhs():
    return urlopen('resources/html/common/menu_rhs.html').read().encode('utf-8').format(uri_servicestatus=uri_servicestatus)