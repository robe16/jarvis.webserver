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
    body = open(os.path.join(os.path.dirname(__file__), '../resources/html/error/error.html'), 'r').read().format(**args)
    #
    return open(os.path.join(os.path.dirname(__file__), '../resources/html/common/header.html'), 'r').read().format(title='Error {code}'.format(code=str(code))) + \
           open(os.path.join(os.path.dirname(__file__), '../resources/html/common/menu_lhs.html'), 'r').read().format(menu='') + \
           open(os.path.join(os.path.dirname(__file__), '../resources/html/common/body.html'), 'r').read().format(header='', body=body) + \
           open(os.path.join(os.path.dirname(__file__), '../resources/html/common/footer.html'), 'r').read()
