import os
from bottle import static_file, HTTPResponse

from parameters import bottle_resource_cache_life
from common_functions.request_log_args import get_request_log_args
from log.log import log_inbound
from resources.global_resources.log_vars import logPass, logException
from resources.global_resources.variables import *


def get_favicon(request):
    #
    args = get_request_log_args(request)
    #
    try:
        #
        status = httpStatusSuccess
        #
        rsp = static_file('favicon.ico',
                          root=os.path.join(os.path.dirname(__file__), '..', 'resources/images/general'))
        rsp.set_header("Cache-Control", "public, max-age={age}".format(age=bottle_resource_cache_life))
        #
        args['result'] = logPass
        args['http_response_code'] = status
        args['description'] = '-'
        log_inbound(**args)
        #
        return rsp
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
        raise HTTPResponse(status=status)
