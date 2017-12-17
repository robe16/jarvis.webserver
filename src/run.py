import sys
from multiprocessing import Process, Manager

from discovery.update_services import update_services
from log.log import log_internal, set_logfile
from portlistener import start_bottle
from resources.lang.enGB.logs import logDescStartingService, logDescPortListener

try:

    ################################
    # Set logfile

    set_logfile()

    ################################

    log_internal(True, logDescStartingService, desc='started')

    services = Manager().dict()

    ################################
    # Receive sys arguments

    # Argument 1: Port of self exposed on host
    try:
        self_port = sys.argv[1]
    except Exception as e:
        self_port = 8080
        #raise Exception('self_hostport not available - {e}'.format(e=e))

    ################################
    # Initiate service broadcast

    process_service_discovery = Process(target=update_services, args=(services, ))
    process_service_discovery.start()

    ################################
    # Port_listener

    log_internal(True, logDescPortListener.format(port=self_port), desc='starting')

    start_bottle(self_port, services)

    process_service_discovery.terminate()

    log_internal(True, logDescPortListener.format(port=self_port), desc='stopped')

except Exception as e:
    log_internal(True, logDescStartingService, desc='fail', exception=e)
