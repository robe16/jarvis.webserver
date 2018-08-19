from log.log import log_internal
from resources.channels.channels import channels
from resources.global_resources.log_vars import logFail, logException


def get_name(channel_id):
    #
    try:
        return channels[channel_id]['name']
    except Exception as e:
        log_internal(logException, 'Could not get image name for \'{chan}\''.format(chan=channel_id), exception=e)
        return ''


def get_image(channel_id, quality='', plus1=False):
    #
    try:
        chan_item = channels[channel_id]
    except Exception as e:
        log_internal(logException, 'Channel id \'{chan}\' not found in list of available resources'.format(chan=channel_id), exception=e)
        return False
    #
    if not quality == '':
        img = _get_image(chan_item, quality, plus1)
        return img if img else False
    else:
        # Default to HD
        img = _get_image(chan_item, 'hd', plus1)
        if img:
            return img
        # Fallback to SD
        img = _get_image(chan_item, 'sd', plus1)
        if img:
            return img
        #
        log_internal(logFail, 'Could not get image name for \'{chan}\''.format(chan=channel_id))
        return False


def _get_image(chan_item, quality, plus1):
    if plus1:
        quality += '_plus1'
    if quality in chan_item['images']:
        return chan_item['images'][quality]
    else:
        return False


def get_category(channel_id):
    #
    try:
        chan_item = channels[channel_id]
    except Exception as e:
        log_internal(logException, 'Channel name \'{chan}\' not found in list of available resources'.format(chan=channel_id), exception=e)
        return False
    #
    return chan_item['category']


def get_sequence_number(channel_id, plus1):
    #
    if plus1:
        seq = 'sequence_plus1'
    else:
        seq = 'sequence'
    #
    try:
        chan_item = channels[channel_id]
    except Exception as e:
        log_internal(logException, 'Channel name \'{chan}\' not found in list of available resources'.format(chan=channel_id), exception=e)
        return False
    #
    return chan_item[seq]


def get_categories():
    return ['Entertainment', 'Movies', 'Sports', 'Factual', 'Lifestyle', 'Kids', 'Music', 'News', 'Radio']
