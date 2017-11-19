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
        groups = ''
        for g in services[s]['groups']:
            groups += ', ' if not groups == '' else ''
            groups += g
        #
        args = {'service_id': services[s]['service_id'],
                'service_name': services[s]['name'],
                'status': status,
                'groups': groups,
                'img': '/img/services/{img}'.format(img=img)}
        #
        page_body += urlopen('resources/html/service_status/service.html').read().encode('utf-8').format(**args)
    #
    if page_body == '':
        page_body = urlopen('resources/html/service_status/service_null.html').read().encode('utf-8')
    else:
        page_body = '<div class="row">{body}</div>'.format(body=page_body)
    #
    return create_page(services,
                       page_body,
                       title='Jarvis',
                       header='Service status')
