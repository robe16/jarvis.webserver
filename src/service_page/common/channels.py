import os
from resources.channels.channels_functions import get_image, get_category, get_sequence_number, get_categories


def createhtml_channels(service, channels):
    #
    _html_categories = {}
    #
    for channel_name in channels['channels']:
        #
        channel = channels['channels'][channel_name]
        #
        try:
            #
            if channel['hd']:
                quality = 'hd'
            elif channel['sd']:
                quality = 'sd'
            else:
                raise Exception
            #
            image = get_image(channel_name, quality)
            #
            if not image and quality == 'hd':
                image = get_image(channel_name, 'sd')
            #
            category = get_category(channel_name)
            #
            if not category in _html_categories.keys():
                _html_categories[category] = {}
            #
            args = {'service_id': service['service_id'],
                    'channel_id': '',
                    'channel_name': channel_name,
                    'channel_image': image,
                    'sendCommand_data': '{{command: \'channel\', channel: \'{channel_name}\'}}'.format(channel_name=channel_name),
                    'cls_highlight': ''}
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/common/channel_grid_item.html'), 'r') as f:
                _html_categories[category][get_sequence_number(channel_name)] = f.read().format(**args)
            #
        except Exception as e:
            pass
    #
    for category in _html_categories.keys():
        #
        _html_category = ''
        for seq_id in sorted(_html_categories[category].keys()):
            _html_category += _html_categories[category][seq_id]
        #
        args = {'category': category,
                'channels': _html_category}
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/common/channel_grid_container.html'), 'r') as f:
            _html_categories[category] = f.read().format(**args)
    #
    pill_first = True
    _html_pill_nav = ''
    _html_pill_contents = ''
    #
    for category in get_categories():
        #
        if pill_first:
            active = 'active'
            pill_first = False
        else:
            active = ''
        #
        args = {'active': active,
                'category': category.lower(),
                'title': category}
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_nav_item.html'), 'r') as f:
            _html_pill_nav += f.read().format(**args)
        #
        #
        args = {'active': active,
                'category': category.lower(),
                'body': _html_categories[category]}
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_content.html'), 'r') as f:
            _html_pill_contents += f.read().format(**args)
        #
    #
    #
    # args = {'title': 'Categories',
    #         'dropdowns': _html_pill_nav}
    # #
    # with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_nav_dropdown.html'), 'r') as f:
    #     _html_pill_nav = f.read().format(**args)
    #
    #
    args = {'nav': _html_pill_nav,
            'content': _html_pill_contents}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_parent.html'), 'r') as f:
        _html = f.read().format(**args)
    #
    return _html
