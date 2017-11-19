serviceName = 'Jarvis: Web Server'
serviceType = 'webserver'

logFileName = 'webserver'
logFileNameTimeformat = '%Y-%m-%d'

logLevelUnset = 'unset'
logLevelDebug = 'debug'
logLevelInfo = 'info'
logLevelWarning = 'warning'
logLevelError = 'error'
logLevelCritical = 'critical'

logCategoryClient = 'client request'
logCategoryProcess = 'process'
logCategoryDevice = 'service'

timeformat = '%Y/%m/%d %H.%M.%S.%f'

uri_home = '/'
uri_servicestatus = '/servicestatus'

uri_servicePage = '/service/page/<service_id>'
uri_serviceCommand = '/service/command/<service_id>'
uri_serviceImage = '/service/image/<service_id>/<filename>'

uri_favicon = '/favicon.ico'
uri_image = '/img/<category>/<filename>'
uri_resource = '/resource/<type>/<filename>'

service_uri_config = '/config'
service_uri_command = '/command'
service_uri_info = '/info/{resource_requested}'

service_uri_lgtvnetcast_image = '/img/appicon/{auid}/{name}'

httpStatusSuccess = 200
httpStatusBadrequest = 400
httpStatusForbidden = 404
httpStatusFailure = 420
httpStatusServererror = 500

jarvis_broadcastPort = 5000
