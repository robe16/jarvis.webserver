serviceName = 'Jarvis: Web Server'
serviceId = 'webserver'
serviceType = 'webserver'

logFileName = 'webserver'
logFileNameTimeformat = '%Y-%m-%d'

# NOTE: delimiter-separated value in log files is '::'
logMsg_Inbound_Info = ':{timestamp}::{serviceid}::{servicetype}::INBOUND::{result}::{client}::{uri}::{method}::{httpresponse}::{desc}'
logMsg_Inbound_Error = ':{timestamp}::{serviceid}::{servicetype}::INBOUND::{result}::{exception}::{client}::{uri}::{method}::{httpresponse}::{desc}'
logMsg_Internal_Info = ':{timestamp}::{serviceid}::{servicetype}::INTERNAL::{result}::{operation}::{desc}'
logMsg_Internal_Error = ':{timestamp}::{serviceid}::{servicetype}::INTERNAL::{result}::{exception}::{operation}::{desc}'
logMsg_Outbound_Info = ':{timestamp}::{serviceid}::{servicetype}::OUTBOUND::{result}::{ip}::{uri}::{method}::{httpresponse}::{desc}'
logMsg_Outbound_Error = ':{timestamp}::{serviceid}::{servicetype}::OUTBOUND::{result}::{exception}::{ip}::{uri}::{method}::{httpresponse}::{desc}'

logPass = 'PASS'
logFail = 'FAIL'
logException = 'EXCEPTION'

timeformat = '%Y/%m/%d %H.%M.%S.%f'

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

jarvis_broadcastPort = 5000
