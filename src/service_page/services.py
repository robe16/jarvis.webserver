import os
from resources.global_resources.variables import projectName
from html.page_body import create_page
from service_page.service.tv_lg_netcast import createPage_tv_lg_netcast
from service_page.service.virginmedia_tivo import createPage_virginmedia_tivo
from service_page.service.nest import createPage_nest
from service_page.service.news import createPage_news


def servicePage(services, service_id):
    #
    resources = '<script src="/resource/js/jarvis.service_page.js"></script>'
    resources += '<script src="/resource/js/jarvis.service_functions.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_page.css">'
    #
    body_html = serviceHtml(services, service_id)
    #
    return create_page(services,
                       body_html,
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
            elif service_type == 'nest':
                page_body = createPage_nest(services[service_id])
            elif service_type == 'news':
                page_body = createPage_news(services[service_id])
            else:
                with open(os.path.join(os.path.dirname(__file__), '../resources/html/services/_unknown.html'), 'r') as f:
                    page_body = f.read().format(service_id=service_id)

        else:
            with open(os.path.join(os.path.dirname(__file__), '../resources/html/services/_offline.html'), 'r') as f:
                page_body = f.read().format(service_id=service_id)
    else:
        with open(os.path.join(os.path.dirname(__file__), '../resources/html/services/_null.html'), 'r') as f:
            page_body = f.read().format(service_id=service_id)
    #
    return page_body