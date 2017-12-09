from log.log import log_internal

# Issue with IDE and production running of script - resolved with try/except below
try:
    # IDE
    from resources.global_resources.channels import channels
except:
    # Production
    from channels import channels


def get_image(channel_name, quality=''):
    #
    try:
        chan_item = channels[channel_name]
    except:
        raise Exception('Channel name \'{chan}\' not found in list of available resources'.format(chan=channel_name))
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
        log_internal(False, 'Could not get image name for \'{chan}\''.format(chan=channel_name), desc='fail')
        return False


def _get_image(chan_item, quality):
    if chan_item[quality]:
        return chan_item[quality]['image']
    else:
        return False
