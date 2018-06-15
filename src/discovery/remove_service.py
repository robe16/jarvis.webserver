from log.log import log_internal
from resources.lang.enGB.logs import logDesc_services_RemoveService
from resources.global_resources.log_vars import logPass, logException


def remove_service(services, service_id):
    try:
        del services[service_id]
        log_internal(logPass, logDesc_services_RemoveService.format(service=service_id))
        return True
    except Exception as e:
        log_internal(logException, logDesc_services_RemoveService.format(service=service_id), exception=e)
        return False
