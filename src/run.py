import sys
from multiprocessing import Process, Manager
from discovery.update_services import update_services
from portlistener import start_bottle
from resources.global_resources.variables import *
from log.log import Log

_log = Log()


try:

    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', '-', 'starting')

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

    _log.new_entry(logCategoryProcess, '-', 'Port listener', 'port-{port}'.format(port=self_port), 'starting')

    start_bottle(self_port, services)

    process_service_discovery.terminate()

    _log.new_entry(logCategoryProcess, '-', 'Port listener', '-'.format(port=self_port), 'stopped')

except Exception as e:
    print('An error has occurred starting micro service: {e}'.format(e=e))
    _log.new_entry(logCategoryProcess, '-', 'Starting micro service', e, 'fail', level=logLevelError)
