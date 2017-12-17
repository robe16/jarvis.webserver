from log.log import log_internal
from groups import groups
from resources.enGB.logs import logDesc_group_NotFound, logDesc_group_ImageNameNotFound


def get_group_list():
    rooms = get_group_rooms_list()
    themes = get_group_themes_list()
    return rooms + themes


def get_group_category_list(cat):
    if cat == 'rooms':
        return get_group_rooms_list()
    elif cat == 'themes':
        return get_group_themes_list()
    else:
        return False


def get_group_rooms_list():
    l = []
    for g in groups['rooms']:
        l.append(g)
    return l


def get_group_themes_list():
    l = []
    for g in groups['themes']:
        l.append(g)
    return l


def get_group_category(group_name):
    #
    group_item = get_group_rooms_details(group_name)
    if group_item:
        return 'rooms'
    #
    group_item = get_group_themes_details(group_name)
    if group_item:
        return 'themes'
    #
    log_internal(False, logDesc_group_NotFound.format(group=group_name), desc='fail')
    return False


def get_group_image(group_name):
    #
    try:
        group_item = get_group_rooms_details(group_name)
        if not group_item:
            group_item = get_group_themes_details(group_name)
        if not group_item:
            raise Exception
    except Exception as e:
        log_internal(False, logDesc_group_NotFound.format(group=group_name), desc='fail')
        return False
    #
    try:
        return group_item['image']
    except Exception as e:
        log_internal(False, logDesc_group_ImageNameNotFound.format(group=group_name), desc='fail')
        return False


def get_group_rooms_details(group_name):
    try:
        return groups['rooms'][group_name]
    except:
        return False


def get_group_themes_details(group_name):
    try:
        return groups['themes'][group_name]
    except:
        return False