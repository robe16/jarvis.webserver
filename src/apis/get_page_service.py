from bottle import HTTPResponse, HTTPError

from service_page.services import servicePage, serviceHtml
from common_functions.request_log_args import get_request_log_args
from log.log import log_inbound
from resources.global_resources.log_vars import logPass, logException
from resources.global_resources.variables import *


def get_page_service(request, services, service_id):
    #
    args = get_request_log_args(request)
    #
    try:
        body_only = (request.query['body'].lower() == 'true')
    except:
        body_only = False
    #
    try:
        #
        if body_only:
            page = serviceHtml(services, service_id)
        else:
            page = servicePage(services, service_id)
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
