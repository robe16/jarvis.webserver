import os
from bottle import HTTPError
from bottle import get, post, error, static_file
from bottle import request, run, HTTPResponse

from resources.global_resources.variables import *
from log.log import Log

from html.home import create_home
from html.error import create_error
from html.service_status import create_servicestatus


def start_bottle(self_port, services):

    _log = Log()

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
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelError)
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
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            return HTTPResponse(body=page, status=status)
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', e, level=logLevelError)
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
            #
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            return rsp
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', e, level=logLevelError)
            raise HTTPError(status)


    ################################################################################################
    # Image files
    ################################################################################################

    # @get(uri_favicon)
    # def get_favicon():
    #     global _server_url
    #     log = log_msg(request, uri_favicon)
    #     #
    #     try:
    #         r = requests.get('{url}/{uri}'.format(url=_server_url, uri='favicon.ico'))
    #         #
    #         log_general(log)
    #         if r.status_code == requests.codes.ok:
    #             return HTTPResponse(status=200, body=r.content)
    #         else:
    #             return HTTPResponse(status=400)
    #         #
    #     except Exception as e:
    #         log_error('{log} - {error}'.format(log=log, error=e))
    #         raise HTTPError(500)


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
            #
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', status, level=logLevelInfo)
            #
            return rsp
            #
        except Exception as e:
            status = httpStatusServererror
            _log.new_entry(logCategoryClient, request['REMOTE_ADDR'], request.url, 'GET', e, level=logLevelError)
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
    _log.new_entry(logCategoryProcess, '-', 'Port listener', '{host}:{port}'.format(host=host, port=self_port), 'started')
    run(host=host, port=self_port, debug=True)
