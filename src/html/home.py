from urllib import urlopen
from resources.global_resources.variables import projectName
from html.page_body import create_page


def create_home(services):
    #
    page_body = urlopen('resources/html/home/home.html').read().encode('utf-8')
    #
    return create_page(services,
                       page_body,
                       title=projectName)