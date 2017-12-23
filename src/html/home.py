import os
from resources.global_resources.variables import projectName
from html.page_body import create_page


def create_home(services):
    #
    resources = '<script src="/resource/js/jarvis.clock.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.clock.css">'
    #
    page_body = open(os.path.join(os.path.dirname(__file__), '../resources/html/home/home.html'), 'r').read()
    #
    return create_page(services,
                       page_body,
                       resources=resources,
                       title=projectName)