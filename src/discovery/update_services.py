from threading import Thread
from discovery.discover_services import discover_services
from discovery.cleanup_services import cleanup_services


def update_services(services):
    #
    thread_discover = Thread(target=discover_services, args=(services,))
    thread_discover.start()
    #
    thread_cleanup = Thread(target=cleanup_services, args=(services,))
    thread_cleanup.start()
    #
    thread_discover.join()
    thread_cleanup.join()
