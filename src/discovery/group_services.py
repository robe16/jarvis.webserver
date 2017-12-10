from resources.groups.groups_functions import get_group_list


def group_services(services):
    #
    grouped_services = {}
    #
    list_groups = get_group_list()
    #
    for list_item in list_groups:
        grouped_services[list_item] = {}
        grouped_services[list_item]['services'] = []
        grouped_services[list_item]['subservices'] = []
        #
        for s in services.keys():
            #
            #  services
            if list_item in services[s]['groups']:
                grouped_services[list_item]['services'].append(services[s]['service_id'])
            #
            #  subservices
            for s_sub in services[s]['subservices']:
                if list_item in s_sub['groups']:
                    temp_sub = {'service_id': services[s]['service_id'],
                                'subservice_id': s_sub['id']}
                    grouped_services[list_item]['services'].append(temp_sub)
        #
    #
    for g in grouped_services:
        if len(grouped_services[g]['services']) == 0 and len(grouped_services[g]['subservices']) == 0:
            del grouped_services[g]
    #
    return grouped_services
