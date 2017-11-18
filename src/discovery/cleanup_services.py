import datetime
from time import sleep
from parameters import discovery_cleanup_expiry, discovery_cleanup_sleep


def cleanup_services(services):
    #
    while True:
        for s in services.keys():
            if services[s]['timestamp'] < (datetime.datetime.now() + datetime.timedelta(seconds=discovery_cleanup_expiry)):
                services[s]['active'] = False
        #
        sleep(discovery_cleanup_sleep)
