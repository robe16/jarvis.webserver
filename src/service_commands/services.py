from service_commands.service.tv_lg_netcast import sendCmd_tv_lg_netcast
from service_commands.service.virginmedia_tivo import sendCmd_virginmedia_tivo
from service_commands.service.nest import sendCmd_nest


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
            elif service_type == 'virginmedia_tivo':
                return sendCmd_virginmedia_tivo(services[service_id], command)
            elif service_type == 'nest':
                return sendCmd_nest(services[service_id], command)
            else:
                return False

        else:
            return False
    else:
        return False
