from bottle import HTTPResponse, HTTPError

from html.home import create_home
from common_functions.request_log_args import get_request_log_args
from log.log import log_inbound
from resources.global_resources.log_vars import logPass, logException
from resources.global_resources.variables import *


def get_home(request, services):
    #
    args = get_request_log_args(request)
    #
    try:
        #
        page = create_home(services)
        #
        status = httpStatusSuccess
        #
        args['result'] = logPass
        args['http_response_code'] = status
        args['description'] = '-'
        log_inbound(**args)
        #
        return HTTPResponse(body=page, status=status)
        #
    except Exception as e:
        #
        status = httpStatusServererror
        #
        args['result'] = logException
        args['http_response_code'] = status
        args['description'] = '-'
        args['exception'] = e
        log_inbound(**args)
        #
        raise HTTPError(status)
