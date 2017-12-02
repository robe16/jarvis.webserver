import sys
from multiprocessing import Process, Manager
from discovery.update_services import update_services
from portlistener import start_bottle
from log.log import log_internal, set_logfile


try:

    ################################
    # Set logfile

    set_logfile()

    ################################

    log_internal(True, 'Starting micro service', desc='started')

    services = Manager().dict()

    ################################
    # Receive sys arguments

    # Argument 1: Port of self exposed on host
    try:
        self_port = sys.argv[1]
    except Exception as e:
        raise Exception('self_hostport not available - {e}'.format(e=e))

    ################################
    # Initiate service broadcast

    process_service_discovery = Process(target=update_services, args=(services, ))
    process_service_discovery.start()

    ################################
    # Port_listener

    log_internal(True, 'Port listener - {port}'.format(port=self_port), desc='starting')

    start_bottle(self_port, services)

    process_service_discovery.terminate()

    log_internal(True, 'Port listener - {port}'.format(port=self_port), desc='stopped')

except Exception as e:
    log_internal(True, 'Starting micro service', desc='fail', exception=e)
