import os
from html.menu import html_menu


def create_page(services, page_body, resources='', title='', header=''):
    #
    return open(os.path.join(os.path.dirname(__file__), '../resources/html/common/header.html'), 'r').read().format(title=title) + \
           html_menu(services) + \
           open(os.path.join(os.path.dirname(__file__), '../resources/html/common/body.html'), 'r').read().format(resources=resources,
                                                                                                                  header=header,
                                                                                                                  body=page_body) + \
           open(os.path.join(os.path.dirname(__file__), '../resources/html/common/footer.html'), 'r').read()
