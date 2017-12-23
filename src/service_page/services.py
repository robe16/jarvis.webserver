from resources.global_resources.variables import projectName
from html.page_body import create_page
from service_page.service.tv_lg_netcast import createPage_tv_lg_netcast
from service_page.service.virginmedia_tivo import createPage_virginmedia_tivo


def servicePage(services, service_id):
    #
    resources = '<script src="/resource/js/jarvis.service_page.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_page.css">'
    #
    return create_page(services,
                       serviceHtml(services, service_id),
                       resources=resources,
                       title='{projectName}: {name}'.format(projectName=projectName,
                                                            name=services[service_id]['name_long']),
                       header=services[service_id]['name_long'])


def serviceHtml(services, service_id):
    #
    if service_id in services.keys():
        #
        if services[service_id]['active']:
            #
            service_type = services[service_id]['service_type']
            #
            if service_type == 'tv_lg_netcast':
                page_body = createPage_tv_lg_netcast(services[service_id])
            elif service_type == 'virginmedia_tivo':
                page_body = createPage_virginmedia_tivo(services[service_id])
            else:
                page_body = open('/resources/html/services/_unknown.html').read().format(service_id=service_id)

        else:
            page_body = open('/resources/html/services/_offline.html').read().format(service_id=service_id)
    else:
        page_body = open('/resources/html/services/_null.html').read().format(service_id=service_id)
    #
    return page_body