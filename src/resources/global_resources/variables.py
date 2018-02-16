projectName = 'Jarvis'

serviceName = 'Jarvis: Web Server'
serviceId = 'webserver'
serviceType = 'webserver'

logFileName = 'webserver'

uri_home = '/'
uri_servicestatus = '/services/status'
uri_service_remove = '/services/remove/<service_id>'

uri_groupPage = '/group/page/<group_id>'

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
service_uri_lgtvnetcast_command_cursorVisbility = '/command/cursor/visibility'
service_uri_lgtvnetcast_command_touchMove = '/command/touch/move'
service_uri_lgtvnetcast_command_touchClick = '/command/touch/click'
service_uri_lgtvnetcast_command_touchWheel = '/command/touch/wheel'
service_uri_lgtvnetcast_apps_all = '/apps/all'
service_uri_lgtvnetcast_3d = '/3d'
service_uri_lgtvnetcast_image_app = '/img/appicon/{auid}'
service_uri_lgtvnetcast_image_screenshot = '/img/screenshot'

service_uri_virginmediativo_channel = '/channel'
service_uri_virginmediativo_recordings = '/recordings'
service_uri_virginmediativo_enterpin = '/enterpin'

service_uri_nest_data_all = '/all'
service_uri_nest_data_structures = '/structures'
service_uri_nest_data_structure_specific = '/structure/{structure_id}'
service_uri_nest_data_devices = '/devices'
service_uri_nest_data_devices_type = '/devices/{device_type}'
service_uri_nest_data_device_specific = '/devices/{device_type}/{device_id}'


service_header_clientid_label = 'jarvis.client-service'

httpStatusSuccess = 200
httpStatusBadrequest = 400
httpStatusForbidden = 404
httpStatusFailure = 420
httpStatusServererror = 500

