from log.log import log_internal
from groups import groups


def get_group_image(group_name):
    #
    try:
        group_item = groups[group_name]
    except Exception as e:
        log_internal(False, 'Group name \'{group}\' not found in list of available resources'.format(group=group_name), desc='fail')
        return False
    #
    try:
        return group_item['image']
    except Exception as e:
        log_internal(False, 'Could not get image name for \'{group}\''.format(group=group_name), desc='fail')
        return False
