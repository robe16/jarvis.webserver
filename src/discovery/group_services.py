from resources.groups.groups_functions import get_group_category_list
from resources.global_resources.logs import logException
from resources.lang.enGB.logs import *
from log.log import log_internal


def group_services(services):
    #
    try:
        categories = {'rooms': {}, 'themes': {}}
        #
        for c, v in categories.items():
            #
            list_groups = get_group_category_list(c)
            #
            grouped_services = {}
            #
            for g in list_groups:
                grouped_services[g] = {}
                grouped_services[g]['services'] = []
                grouped_services[g]['subservices'] = []
                #
                for s, v in services.items():
                    #
                    #  services
                    if g in services[s]['groups']:
                        grouped_services[g]['services'].append(services[s]['service_id'])
                    #
                    #  subservices
                    for s_sub in services[s]['subservices']:
                        if g in s_sub['groups']:
                            temp_sub = {'service_id': services[s]['service_id'],
                                        'subservice_id': s_sub['id']}
                            grouped_services[g]['services'].append(temp_sub)
            #
            for g in list(grouped_services.keys()):
                if len(grouped_services[g]['services']) == 0 and len(grouped_services[g]['subservices']) == 0:
                    del grouped_services[g]
            #
            categories[c] = grouped_services
        #
        return categories
        #
    except Exception as e:
        log_internal(logException, logDesc_groupServices, exception=e)
        return False
