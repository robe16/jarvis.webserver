from urllib import urlopen
from html.menu import html_menu


def create_page(services, page_body, page_javascript='', title='', header=''):
    #
    return urlopen('resources/html/common/header.html').read().encode('utf-8').format(title=title) +\
           html_menu(services) +\
           urlopen('resources/html/common/body.html').read().encode('utf-8').format(page_javascript=page_javascript,
                                                                                    header=header,
                                                                                    body=page_body) +\
           urlopen('resources/html/common/footer.html').read().encode('utf-8')
