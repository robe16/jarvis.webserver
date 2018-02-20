from log.log import log_internal
from resources.channels.channels import channels
from resources.global_resources.logs import logFail, logException


def get_image(channel_name, quality=''):
    #
    try:
        chan_item = channels[channel_name]
    except Exception as e:
        log_internal(logException, 'Channel name \'{chan}\' not found in list of available resources'.format(chan=channel_name), exception=e)
        return False
    #
    if not quality == '':
        img = _get_image(chan_item, quality)
        return img if img else False
    else:
        # Default to HD
        img = _get_image(chan_item, 'hd')
        if img:
            return img
        # Fallback to SD
        img = _get_image(chan_item, 'sd')
        if img:
            return img
        #
        log_internal(logFail, 'Could not get image name for \'{chan}\''.format(chan=channel_name))
        return False


def _get_image(chan_item, quality):
    if chan_item[quality]:
        return chan_item[quality]['image']
    else:
        return False


def get_category(channel_name):
    #
    try:
        chan_item = channels[channel_name]
    except Exception as e:
        log_internal(logException, 'Channel name \'{chan}\' not found in list of available resources'.format(chan=channel_name), exception=e)
        return False
    #
    return chan_item['category']

def get_categories():
    return ['Entertainment', 'Movies', 'Sports', 'Factual', 'Lifestyle', 'Kids', 'Music', 'News', 'Radio']
