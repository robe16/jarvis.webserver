from urllib import urlopen

from html.page_body import create_page
from service_page.service.tv_lg_netcast import createPage_tv_lg_netcast


def servicePage(services, service_id):
    #
    if service_id in services.keys():
        #
        if services[service_id]['active']:
            #
            service_type = services[service_id]['service_type']
            #
            if service_type == 'tv_lg_netcast':
                page_body = createPage_tv_lg_netcast(services[service_id])
            else:
                page_body = urlopen('resources/html/services/_unknown.html').read().encode('utf-8').format(service_id=service_id)

        else:
            page_body = urlopen('resources/html/services/_offline.html').read().encode('utf-8').format(service_id=service_id)
    else:
        page_body = urlopen('resources/html/services/_null.html').read().encode('utf-8').format(service_id=service_id)
    #
    return create_page(services,
                       page_body,
                       title='Jarvis')