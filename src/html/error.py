import os

def create_error(code):
    if code == 404:
        args = {'code': '404',
                'desc': 'Page not found',
                'mesg': 'The page you are looking for does not exist!!'}
    elif code == 500:
        args = {'code': '500',
                'desc': 'Network error',
                'mesg': 'There was an error with the code on the server!!'}
    else:
        args = {'code': '---',
                'desc': 'Unknown',
                'mesg': 'An error has been encountered, please try again!!'}
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/error/error.html'), 'r') as f:
        body = f.read().format(**args)
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/body.html'), 'r') as f:
        body = f.read().format(resources='', header='', body=body)
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/header.html'), 'r') as f:
        header = f.read().format(title='Error {code}'.format(code=str(code)))
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_lhs.html'), 'r') as f:
        menu = f.read().format(menu='')
    #
    with open(os.path.join(os.path.dirname(__file__), '../resources/html/common/footer.html'), 'r') as f:
        footer = f.read()
    #
    return '{header}{menu}{body}{footer}'.format(header=header,
                                                 menu=menu,
                                                 body=body,
                                                 footer=footer)
