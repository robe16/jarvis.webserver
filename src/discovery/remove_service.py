from log.log import log_internal


def remove_service(services, service_id):
    try:
        del services[service_id]
        log_internal(True, 'Removal of service \'{service}\' from discovered service dictionary'.format(service=service_id), desc='success')
        return True
    except Exception as e:
        log_internal(False, 'Removal of service \'{service}\' from discovered service dictionary'.format(service=service_id), desc='fail', exception=e)
        return False