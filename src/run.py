from multiprocessing import Process, Manager

from config.config import get_cfg_port_listener
from discovery.update_services import update_services
from log.log import log_internal, set_logfile
from portlistener import start_bottle
from resources.lang.enGB.logs import logDescStartingService, logDescPortListener

port_threads = []

try:

    ################################
    # Set logfile

    set_logfile()

    ################################

    log_internal(True, logDescStartingService, desc='started')

    services = Manager().dict()

    ################################
    # Initiate service broadcast

    process_service_discovery = Process(target=update_services, args=(services, ))
    process_service_discovery.start()

    ################################
    # Port_listener

    log_internal(True, logDescPortListener.format(port=get_cfg_port_listener()), desc='starting')

    start_bottle(port_threads, services)

    process_service_discovery.terminate()

    log_internal(True, logDescPortListener.format(port=get_cfg_port_listener()), desc='stopped')

except Exception as e:
    log_internal(True, logDescStartingService, desc='fail', exception=e)
    for t in port_threads:
        t._stop()
