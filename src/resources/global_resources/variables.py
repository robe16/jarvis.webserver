serviceName = 'Jarvis: Web Server'
serviceId = 'webserver'
serviceType = 'webserver'

logFileName = 'webserver'

uri_home = '/'
uri_servicestatus = '/services/status'

uri_servicePage = '/service/page/<service_id>'
uri_serviceCommand = '/service/command/<service_id>'
uri_serviceImage = '/service/image/<service_id>/<filename>'

uri_favicon = '/favicon.ico'
uri_image = '/img/<category>/<filename>'
uri_resource = '/resource/<type>/<filename>'

service_uri_config = '/config'
service_uri_command = '/command'

service_uri_lgtvnetcast_command_keyInput = '/command/keyInput'
service_uri_lgtvnetcast_command_executeApp = '/command/executeApp'
service_uri_lgtvnetcast_apps_all = '/apps/all'
service_uri_lgtvnetcast_image = '/img/appicon/{auid}'

service_uri_virginmediativo_channel = '/channel'
service_uri_virginmediativo_recordings = '/recordings'

service_header_clientid_label = 'jarvis.client-service'

httpStatusSuccess = 200
httpStatusBadrequest = 400
httpStatusForbidden = 404
httpStatusFailure = 420
httpStatusServererror = 500

service_status_active_header = 'Active'
service_status_active_note = 'Services that have been detected within the last two minutes.'
service_status_mia_header = 'MIA'
service_status_mia_note = 'Services that have not been detected within the last two minutes.'

service_status_active_none_msg = 'No services have been identified during discovery.'
service_status_mia_none_msg = 'All services have been deteceted within the last two minutes.'
service_status_none_note = 'Please refresh this page for an update.'
