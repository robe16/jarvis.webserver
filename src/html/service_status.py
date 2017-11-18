from urllib import urlopen
from html.page_body import create_page


def create_servicestatus(services):
    #
    page_body = ''
    #
    for s in services.keys():
        #
        type = services[s]['service_type']
        #
        if type == 'tv_lg_netcast':
            img = 'logo_lg.png'
        else:
            img = 'logo_other.png'
        #
        status = 'Online' if services[s]['active'] else 'Offline'
        #
        args = {'service_name': services[s]['name'],
                'status': status,
                'groups': services[s]['groups'],
                'img': '/img/services/{img}'.format(img=img)}
        #
        page_body += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
    #
    if page_body == '':
        page_body = urlopen('resources/html/service_status/service_null.html').read().encode('utf-8')
    #
    return create_page(services,
                       page_body,
                       title='Jarvis',
                       header='Service status')
