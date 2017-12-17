from log.log import log_internal
from resources.lang.enGB.logs import logDesc_services_RemoveService


def remove_service(services, service_id):
    try:
        del services[service_id]
        log_internal(True, logDesc_services_RemoveService.format(service=service_id), desc='success')
        return True
    except Exception as e:
        log_internal(False, logDesc_services_RemoveService.format(service=service_id), desc='fail', exception=e)
        return False