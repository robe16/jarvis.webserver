import os
from html.menu import html_menu


def create_page(services, page_body, resources='', title='', header=''):
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/body.html'), 'r') as f:
        body = f.read().format(resources=resources, header=header, body=page_body)
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/header.html'), 'r') as f:
        header = f.read().format(title=title)
    #
    menu = html_menu(services)
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/footer.html'), 'r') as f:
        footer = f.read()
    #
    return '{header}{menu}{body}{footer}'.format(header=header,
                                                 menu=menu,
                                                 body=body,
                                                 footer=footer)