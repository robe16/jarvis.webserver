from service_commands.service.tv_lg_netcast import sendCmd_tv_lg_netcast


def serviceCommand(services, service_id, command):
    #
    if service_id in services.keys():
        #
        if services[service_id]['active']:
            #
            service_type = services[service_id]['service_type']
            #
            if service_type == 'tv_lg_netcast':
                return sendCmd_tv_lg_netcast(services[service_id], command)
            else:
                return False

        else:
            return False
    else:
        return False
