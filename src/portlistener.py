import os

from bottle import HTTPError
from bottle import get, post, delete, static_file
from bottle import request, run, HTTPResponse

from discovery.remove_service import remove_service

from html.home import create_home
from html.service_status import create_servicestatus
from log.log import log_inbound, log_internal
from resources.global_resources.variables import *
from parameters import bottle_resource_cache_life

from service_commands.services import serviceCommand
from service_images.services import serviceImage
from service_page.services import servicePage
from service_page.groups import groupPage


def start_bottle(self_port, services):

    ################################################################################################
    # Enable cross domain scripting
    ################################################################################################

    def enable_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        return response

    ################################################################################################
    # Home
    ################################################################################################

    @get(uri_home)
    def get_home():
        try:
            #
            page = create_home(services)
            #
            status = httpStatusSuccess
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)

    ################################################################################################
    # Service Status
    ################################################################################################

    @get(uri_servicestatus)
    def get_servicestatus():
        try:
            #
            page = create_servicestatus(services)
            #
            status = httpStatusSuccess
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)

    @delete(uri_service_remove)
    def delete_removeService(service_id):
        try:
            #
            rsp = remove_service(services, service_id)
            #
            status = httpStatusSuccess if rsp else httpStatusFailure
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'DELETE', status)
            #
            return HTTPResponse(status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'DELETE', status, exception=e)
            raise HTTPError(status)

    ################################################################################################
    # Groups
    ################################################################################################

    @get(uri_groupPage)
    def get_groupPage(group_id):
        try:
            #
            page = groupPage(services, group_id)
            #
            status = httpStatusSuccess
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)

    ################################################################################################
    # Services
    ################################################################################################

    @get(uri_servicePage)
    def get_servicePage(service_id):
        try:
            #
            page = servicePage(services, service_id)
            #
            status = httpStatusSuccess
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)

    @post(uri_serviceCommand)
    def post_serviceCommand(service_id):
        try:
            #
            command = request.json
            #
            rsp = serviceCommand(services, service_id, command)
            #
            status = httpStatusSuccess if rsp else httpStatusFailure
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'POST', status, desc=request.json)
            #
            return HTTPResponse(status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'POST', status, desc=request.json, exception=e)
            raise HTTPError(status)

    @get(uri_serviceImage)
    def get_serviceImage(service_id, filename):
        try:
            #
            query = request.query
            #
            rsp = serviceImage(services, service_id, filename, query)
            rsp.set_header("Cache-Control", "public, max-age={age}".format(age=bottle_resource_cache_life))
            #
            status = httpStatusSuccess if bool(rsp) else httpStatusFailure
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status, desc=_convert_query_to_string(request.query))
            #
            return HTTPResponse(body=rsp, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, desc=_convert_query_to_string(request.query), exception=e)
            raise HTTPError(status)


    ################################################################################################
    # Resources
    ################################################################################################

    @get(uri_resource)
    def get_resource(type, filename):
        try:
            #
            status = httpStatusSuccess
            #
            rsp = static_file(filename, root=os.path.join(os.path.dirname(__file__),
                                                          ('resources/static/{folder}'.format(folder=type))))
            rsp.set_header("Cache-Control", "public, max-age={age}".format(age=bottle_resource_cache_life))
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return rsp
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)


    ################################################################################################
    # Image files
    ################################################################################################

    @get(uri_favicon)
    def get_favicon():
        #
        try:
            #
            status = httpStatusSuccess
            #
            rsp = static_file('favicon.ico',
                              root=os.path.join(os.path.dirname(__file__), 'resources/images/general'))
            rsp.set_header("Cache-Control", "public, max-age={age}".format(age=bottle_resource_cache_life))
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return rsp
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)


    @get(uri_image)
    def get_image(category, filename):
        #
        try:
            #
            status = httpStatusSuccess
            #
            root = os.path.join(os.path.dirname(__file__), 'resources/images/{category}'.format(category=category))
            mimetype = filename.split('.')[1]
            #
            rsp = static_file(filename,
                              root=root,
                              mimetype='image/{mimetype}'.format(mimetype=mimetype))
            rsp.set_header("Cache-Control", "public, max-age={age}".format(age=bottle_resource_cache_life))
            #
            log_inbound(True, request['REMOTE_ADDR'], request.url, 'GET', status)
            #
            return rsp
            #
        except Exception as e:
            status = httpStatusServererror
            log_inbound(False, request['REMOTE_ADDR'], request.url, 'GET', status, exception=e)
            raise HTTPError(status)

    ################################################################################################
    # Error pages/responses
    ################################################################################################

    # @error(404)
    # def error404(error):
    #     return HTTPResponse(body=create_error(404), status=404)


    # @error(500)
    # def error500(error):
    #     return HTTPResponse(body=create_error(500), status=500)


    ################################################################################################

    host='0.0.0.0'
    log_internal(True, 'Port listener', desc='started')
    run(host=host, port=self_port, debug=True)


def _convert_query_to_string(bottleDict):
    #
    str = '{'
    for k in bottleDict:
        str += ', ' if not str == '{' else ''
        str += '"{key}":"{value}"'.format(key=k, value=bottleDict[k])
    str += '}'
    #
    return str
