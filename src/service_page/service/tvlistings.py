import os
import datetime
import requests
from resources.global_resources.variables import *
from resources.global_resources.logs import logPass, logFail
from resources.channels.channels import channels
from resources.channels.channels_functions import get_image, get_category, get_sequence_number, get_categories
from log.log import log_outbound


def createPage_tvlistings(service):
    #
    resources = '<link rel="stylesheet" href="/resource/css/jarvis.service_page.tvlistings.css">'
    #
    html_buttons = ''
    html_body = ''
    #
    # TVListings
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='12',
                                        service_id=service['service_id'],
                                        function_id='tvlistings',
                                        function_name='TV Listings',
                                        btn_class='service_function_btn_active')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='tvlistings',
                                     function_body=_html_tvlistings(service),
                                     body_class='service_function_body_active')
    #
    args = {'service_id': service['service_id'],
            'resources': resources,
            'html_buttons': html_buttons,
            'html_body': html_body}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_container.html'), 'r') as f:
        page_body = f.read().format(**args)
    #
    return page_body


hourly_width_px = 400
max_hours = 6
isoformat = '%Y-%m-%d %H:%M:%S'
time_format = '%H:%M'


def _html_tvlistings(service):
    #
    _listings = _get_listings(service)
    #
    if not str(_listings)=='False':
        args = {'timestamp': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'body_tvlistings': _create_html(service, _listings)}
    else:
        args = {'timestamp': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'body_tvlistings': 'ERROR'}
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listings_container.html'), 'r') as f:
        _return = f.read().format(**args)
    #
    return _return


def _create_html(service, _listings):
    #
    current_hour = datetime.datetime.now().hour
    current_hourly_time = datetime.datetime.combine(datetime.date.today(),
                                                    datetime.time(current_hour))
    #
    html_hours_title = ''
    for x in range(0, (2 * max_hours) + 1, 1):
        hr = int(float(x)/2)
        mn = int((float(x)/2 - hr) * 60)
        t = current_hourly_time + datetime.timedelta(hours=hr, minutes=mn)
        args_time = {'width': hourly_width_px/2,
                     'hour': t.strftime(time_format)}
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listing_title.html'), 'r') as f:
            html_hours_title += f.read().format(**args_time)
        #
    #
    # vertical line for now() time
    left_dist = _calc_item_width(current_hourly_time, datetime.datetime.now())
    #
    first_tab = True
    html_pill_nav = ''
    html_pill_contents = ''
    #
    #
    html_channels = {}
    html_listings = {}
    #
    #
    for chan_name in channels:
        #
        category = get_category(chan_name)
        #
        if not category in html_channels.keys():
            html_channels[category] = {}
            html_listings[category] = {}
        #
        logo = get_image(chan_name)
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/channel_item.html'), 'r') as f:
            html_channels[category][get_sequence_number(chan_name)] = f.read().format(imgchan=logo)
        #
        # Create listing items
        try:
            if len(_listings[chan_name]) > 0:
                #
                temp_html = ''
                item_keys = sorted(_listings[chan_name].keys())
                #
                for item in item_keys:
                    #
                    start = datetime.datetime.strptime(_listings[chan_name][item]['start'], isoformat)
                    end = datetime.datetime.strptime(_listings[chan_name][item]['end'], isoformat)
                    #
                    if (start > current_hourly_time or end > current_hourly_time) and start < (current_hourly_time + datetime.timedelta(hours=max_hours)):
                        #
                        if start < current_hourly_time:
                            width_s = current_hourly_time
                        else:
                            width_s = start
                        #
                        if end > current_hourly_time + datetime.timedelta(hours=max_hours):
                            width_e = current_hourly_time + datetime.timedelta(hours=max_hours)
                        else:
                            width_e = end
                        #
                        item_width = _calc_item_width(width_s, width_e)
                        #
                        subtitle = ''
                        try:
                            if _listings[chan_name][item]['subtitle'] != '':
                                subtitle = '{subtitle}: '.format(subtitle=_listings[chan_name][item]['subtitle'])
                        except Exception as e:
                            pass
                        #
                        args_item = {'width': item_width - 2,
                                     'start': start.strftime(time_format),
                                     'end': end.strftime(time_format),
                                     'title': _listings[chan_name][item]['title'],
                                     'subtitle': subtitle,
                                     'desc': _listings[chan_name][item]['desc']}
                        #
                        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listing_item.html'), 'r') as f:
                            temp_html += f.read().format(**args_item)
            else:
                raise Exception
            #
            args_listings = {'listings': temp_html}
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listing_row.html'), 'r') as f:
                html_listings[category][get_sequence_number(chan_name)] = f.read().format(**args_listings)
            #
        except Exception as e:
            args_listings = {'listings': '<div style="padding: 5px;">No listings available</div>'}
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listing_row.html'), 'r') as f:
                html_listings[category][get_sequence_number(chan_name)] = f.read().format(**args_listings)
    #
    #
    try:
        # Create pills nav items for each category item
        for category in get_categories():
            #
            if first_tab:
                active = 'active'
                first_tab = False
            else:
                active = ''
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_nav_item.html'), 'r') as f:
                html_pill_nav += f.read().format(active=active,
                                                 category='{service}_{category}'.format(service=service['service_id'],
                                                                                        category=category).lower(),
                                                 title=category)
            #
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/channel_title.html'), 'r') as f:
                html_channels_final = f.read()
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listing_row.html'), 'r') as f:
                html_listings_final = f.read().format(listings=html_hours_title)
            #
            #
            for num in sorted(html_channels[category].keys()):
                html_channels_final += html_channels[category][num]
                html_listings_final += html_listings[category][num]
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/tvlistings/listings_body.html'), 'r') as f:
                html_pill_body = f.read().format(left_dist=left_dist,
                                                 rows_channel_images=html_channels_final,
                                                 rows_listings=html_listings_final)
            #
            with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_content.html'), 'r') as f:
                html_pill_contents += f.read().format(active=active,
                                                      category='{service}_{category}'.format(service=service['service_id'],
                                                                                             category=category).lower(),
                                                      body=html_pill_body)
        #
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/common/pill_parent.html'), 'r') as f:
            _return = f.read().format(nav=html_pill_nav,
                                      content=html_pill_contents)
        #
        return _return
    except Exception as e:
        return e


def _calc_item_width(start, end):
    hours_diff = (end - start).total_seconds()/3600
    return hourly_width_px * hours_diff


def _get_listings(service):
    #
    uri = service_uri_tvlistings_all
    #
    try:
        #
        service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                       port=service['port'],
                                                       uri=uri)
        #
        headers = {service_header_clientid_label: serviceId}
        r = requests.get(service_url, headers=headers)
        #
        if r.status_code == requests.codes.ok:
            log_outbound(logPass,
                         service['ip'], service['port'], 'GET', uri,
                         '-', '-',
                         r.status_code)
            return r.json()
        else:
            log_outbound(logFail,
                         service['ip'], service['port'], 'GET', uri,
                         '-', '-',
                         r.status_code)
            return {}
    except Exception as e:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', uri,
                     '-', '-',
                     '-',
                     exception=e)
        return {}
