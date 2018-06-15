from bottle import HTTPResponse, HTTPError

from validation.validation import validate_tv_lg_netcast, validate_virginmedia_tivo, validate_xbox_one, validate_nest
from service_commands.services import serviceCommand
from common_functions.request_log_args import get_request_log_args
from log.log import log_inbound
from resources.global_resources.log_vars import logPass, logException
from resources.global_resources.variables import *


def post_service_command(request, services, service_id):
    #
    args = get_request_log_args(request)
    #
    service_type = services[service_id]['service_type']
    #
    try:
        #
        command = request.json
        #
        if service_type == 'tv_lg_netcast':
            validation_pass = validate_tv_lg_netcast(command)
        elif service_type == 'virginmedia_tivo':
            validation_pass = validate_virginmedia_tivo(command)
        elif service_type == 'xbox_one':
            validation_pass = validate_xbox_one(command)
        elif service_type == 'nest':
            validation_pass = validate_nest(command)
        else:
            validation_pass = False
        #
        if validation_pass:
            rsp = serviceCommand(services, service_id, command)
            status = httpStatusSuccess if rsp else httpStatusFailure
        else:
            status = httpStatusBadrequest
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
