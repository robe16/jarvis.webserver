from html.menu import html_menu


def create_page(services, page_body, resources='', title='', header=''):
    #
    return open('resources/html/common/header.html', 'r').read().format(title=title) + \
           html_menu(services) +\
           open('resources/html/common/body.html', 'r').read().format(resources=resources,
                                                                      header=header,
                                                                      body=page_body) + \
           open('resources/html/common/footer.html', 'r').read()
