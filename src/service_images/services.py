from service_images.service.tv_lg_netcast import getImage_tv_lg_netcast


def serviceImage(services, service_id, filename, query):
    #
    if service_id in services.keys():
        #
        if services[service_id]['active']:
            #
            service_type = services[service_id]['service_type']
            #
            if service_type == 'tv_lg_netcast':
                return getImage_tv_lg_netcast(services[service_id], filename, query)
            else:
                return False
    return False
