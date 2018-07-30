from bottle import error
from bottle import get, post, delete
from bottle import request, run, HTTPResponse

from config.config import get_cfg_port
from html.error import create_error
from log.log import log_internal
from resources.global_resources.log_vars import logPass
from resources.lang.enGB.logs import logDescPortListener

from apis.get_home import get_home
from apis.get_servicestatus import get_servicestatus
from apis.delete_removeService import delete_removeService
from apis.get_page_group import get_page_group
from apis.get_page_service import get_page_service
from apis.post_service_command import post_service_command
from apis.get_service_image import get_service_image
from apis.get_resource import get_resource
from apis.get_image import get_image
from apis.get_favicon import get_favicon


def start_bottle(services):

    ################################################################################################
    # APIs
    ################################################################################################

    @get('/')
    def api_get_home():
        return get_home(request, services)

    @get('/services/status')
    def api_get_servicestatus():
        return get_servicestatus(request, services)

    @delete('/services/remove/<service_id>')
    def api_delete_removeService(service_id):
        return delete_removeService(request, services, service_id)

    @get('/group/page/<group_id>')
    def api_get_page_group(group_id):
        return get_page_group(request, services, group_id)

    @get('/service/page/<service_id>')
    def api_get_page_service(service_id):
        return get_page_service(request, services, service_id)

    @post('/service/command/<service_id>')
    def api_post_service_command(service_id):
        return post_service_command(request, services, service_id)

    @get('/service/image/<service_id>/<filename>')
    def api_get_service_image(service_id, filename):
        return get_service_image(request, services, service_id, filename)

    @get('/resource/<type>/<filename>')
    def api_get_resource(type, filename):
        return get_resource(request, type, filename)

    @get('/img/<category>/<filename>')
    def api_get_image(category, filename):
        return get_image(request, category, filename)

    @get('/favicon.ico')
    def api_get_favicon():
        return get_favicon(request)

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

    host = 'localhost'
    port = get_cfg_port()
    run(host=host, port=port, server='paste', debug=True)

    log_internal(logPass, logDescPortListener.format(port=port), description='started')

    ################################################################################################
