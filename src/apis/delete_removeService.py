from bottle import HTTPResponse, HTTPError

from discovery.remove_service import remove_service
from common_functions.request_log_args import get_request_log_args
from log.log import log_inbound
from resources.global_resources.log_vars import logPass, logException
from resources.global_resources.variables import *


def delete_removeService(request, services, service_id):
    #
    args = get_request_log_args(request)
    #
    try:
        #
        rsp = remove_service(services, service_id)
        #
        status = httpStatusSuccess if rsp else httpStatusFailure
        #
        args['result'] = logPass
        args['http_response_code'] = status
        args['description'] = '-'
        log_inbound(**args)
        #
        return HTTPResponse(status=status)
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
