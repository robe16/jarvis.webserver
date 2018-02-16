import os
import threading
from bottle import HTTPError, error
from bottle import get, post, delete, static_file
from bottle import request, run, HTTPResponse

from common_functions.query_to_string import convert_query_to_string
from config.config import get_cfg_port_listener
from discovery.remove_service import remove_service
from html.error import create_error
from html.home import create_home
from html.service_status import create_servicestatus
from log.log import log_inbound, log_internal
from parameters import bottle_resource_cache_life
from resources.global_resources.variables import *
from resources.global_resources.logs import logException, logPass
from resources.lang.enGB.logs import logDescPortListener
from service_commands.services import serviceCommand
from service_images.services import serviceImage
from service_page.groups import groupPage
from service_page.services import servicePage, serviceHtml


def start_bottle(port_threads, services):

    ################################################################################################
    # Enable cross domain scripting
    ################################################################################################

    def enable_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET'
        return response

    ################################################################################################
    # Log arguments
    ################################################################################################

    def _get_log_args(request):
        #
        urlparts = request.urlparts
        #
        try:
            client_ip = request.headers['X-Forwarded-For']
        except:
            client_ip = request['REMOTE_ADDR']
        #
        try:
            server_ip = request.headers['X-Real-IP']
        except:
            server_ip = urlparts.hostname
        #
        server_request_query = convert_query_to_string(request.query) if request.query_string else '-'
        server_request_body = request.body.read() if request.body.read()!='' else '-'
        #
        return {'client_ip': client_ip,
                'client_user': '-',
                'server_ip': server_ip,
                'server_thread_port': urlparts.port,
                'server_method': request.method,
                'server_request_uri': urlparts.path,
                'server_request_query': server_request_query,
                'server_request_body': server_request_body}


    ################################################################################################
    # Home
    ################################################################################################

    @get(uri_home)
    def get_home():
        #
        args = _get_log_args(request)
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

    ################################################################################################
    # Service Status
    ################################################################################################

    @get(uri_servicestatus)
    def get_servicestatus():
        #
        args = _get_log_args(request)
        #
        try:
            #
            page = create_servicestatus(services)
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

    @delete(uri_service_remove)
    def delete_removeService(service_id):
        #
        args = _get_log_args(request)
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

    ################################################################################################
    # Groups
    ################################################################################################

    @get(uri_groupPage)
    def get_groupPage(group_id):
        #
        args = _get_log_args(request)
        #
        try:
            #
            page = groupPage(services, group_id)
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

    ################################################################################################
    # Services
    ################################################################################################

    @get(uri_servicePage)
    def get_servicePage(service_id):
        #
        args = _get_log_args(request)
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

    @post(uri_serviceCommand)
    def post_serviceCommand(service_id):
        #
        args = _get_log_args(request)
        #
        try:
            #
            command = request.json
            #
            rsp = serviceCommand(services, service_id, command)
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

    @get(uri_serviceImage)
    def get_serviceImage(service_id, filename):
        #
        args = _get_log_args(request)
        #
        try:
            #
            query = request.query
            #
            img = serviceImage(services, service_id, filename, query)
            #
            status = httpStatusSuccess if bool(img) else httpStatusFailure
            #
            rsp = HTTPResponse(body=img, status=status)
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
            raise HTTPError(status)


    ################################################################################################
    # Resources
    ################################################################################################

    @get(uri_resource)
    def get_resource(type, filename):
        #
        args = _get_log_args(request)
        #
        try:
            #
            status = httpStatusSuccess
            #
            rsp = static_file(filename, root=os.path.join(os.path.dirname(__file__),
                                                          ('resources/static/{folder}'.format(folder=type))))
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
            raise HTTPError(status)


    ################################################################################################
    # Image files
    ################################################################################################

    @get(uri_favicon)
    def get_favicon():
        #
        args = _get_log_args(request)
        #
        try:
            #
            status = httpStatusSuccess
            #
            rsp = static_file('favicon.ico',
                              root=os.path.join(os.path.dirname(__file__), 'resources/images/general'))
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
            raise HTTPError(status)


    @get(uri_image)
    def get_image(category, filename):
        #
        args = _get_log_args(request)
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
            raise HTTPError(status)

    ################################################################################################
    # Error pages/responses
    ################################################################################################

    @error(404)
    def error404(error):
        return HTTPResponse(body=create_error(404), status=404)


    @error(500)
    def error500(error):
        return HTTPResponse(body=create_error(500), status=500)


    ################################################################################################

    def bottle_run(x_host, x_port):
        log_internal(logPass, logDescPortListener.format(port=x_port), description='started')
        run(host=x_host, port=x_port, debug=True)

    ################################################################################################

    host = 'localhost'
    ports = get_cfg_port_listener()
    for port in ports:
        t = threading.Thread(target=bottle_run, args=(host, port,))
        port_threads.append(t)

    # Start all threads
    for t in port_threads:
        t.start()
    # Use .join() for all threads to keep main process 'alive'
    for t in port_threads:
        t.join()
