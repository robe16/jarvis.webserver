from multiprocessing import Process, Manager

from config.config import get_cfg_port
from discovery.update_services import update_services
from log.log import log_internal
from portlistener import start_bottle
from resources.lang.enGB.logs import logDescStartingService, logDescPortListener
from resources.global_resources.log_vars import logPass, logException


try:

    ################################

    log_internal(logPass, logDescStartingService, description='started')

    services = Manager().dict()

    ################################
    # Initiate service broadcast

    process_service_discovery = Process(target=update_services, args=(services, ))
    process_service_discovery.start()

    ################################
    # Port_listener

    log_internal(logPass, logDescPortListener.format(port=get_cfg_port()), description='starting')

    start_bottle(services)

    process_service_discovery.terminate()

    log_internal(logPass, logDescPortListener.format(port=get_cfg_port()), description='stopped')

except Exception as e:
    log_internal(logException, logDescStartingService, description='fail', exception=e)
