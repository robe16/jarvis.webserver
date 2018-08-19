import os
import requests

from log.log import log_outbound, log_internal
from resources.global_resources.log_vars import logPass, logFail, logException
from resources.channels.channels_functions import get_image
from resources.global_resources.variables import *
from resources.lang.enGB.logs import *
from service_page.common.channels import createhtml_channels


def createPage_virginmedia_tivo(service):
    #
    resources = '<link rel="stylesheet" href="/resource/css/jarvis.service_page.channels.css">'
    #
    html_buttons = ''
    html_body = ''
    #
    # Controls
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='4',
                                        service_id=service['service_id'],
                                        function_id='remote',
                                        function_name='Remote',
                                        btn_class='service_function_btn_active')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='remote',
                                     function_body=_html_controls(service),
                                     body_class='service_function_body_active')
    #
    # Recordings
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='4',
                                        service_id=service['service_id'],
                                        function_id='recordings',
                                        function_name='Recordings',
                                        btn_class='')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='recordings',
                                     function_body=_html_recordings(service),
                                     body_class='')
    #
    # Channels
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
        html_buttons += f.read().format(width='4',
                                        service_id=service['service_id'],
                                        function_id='channels',
                                        function_name='Channels',
                                        btn_class='')
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
        html_body += f.read().format(service_id=service['service_id'],
                                     function_id='channels',
                                     function_body=_html_channels(service),
                                     body_class='')
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


def _html_channels(service):
    #
    current_chan = _current_chan(service)
    channels = _get_channels(service)
    html_channels = createhtml_channels(service, channels)
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/virginmedia_tivo/channels.html'), 'r') as f:
        args = {'now_viewing_logo': current_chan['logo'],
                'now_viewing': current_chan['name'],
                'html_channels': html_channels}
        _html = f.read().format(**args)
    #
    return _html


def _current_chan(service):
    #
    chan_current = _get_current_chan(service)
    #
    if bool(chan_current):
        current_chan = {'name': chan_current['channel']['name'],
                        'logo': get_image(chan_current['channel']['name'],
                                          chan_current['channel']['quality'])}
    else:
        current_chan = {'name': '-',
                        'logo': '_blank.png'}
    #
    return current_chan


def _html_controls(service):
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/virginmedia_tivo/controls.html'), 'r') as f:
        html_controls = f.read().format(service_id=service['service_id'])
    #
    return html_controls


def _html_recordings(service):
    #
    recordings = _get_recordings(service)
    #
    with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/virginmedia_tivo/recordings.html'), 'r') as f:
        args = {'html_recordings': _recordings(recordings),
                'timestamp_recordings': recordings['timestamp']}
        html_recordings = f.read().format(**args)
    #
    return html_recordings


def _recordings(json_recordings):
    #
    html_recordings = ''
    #
    try:
        #
        if not json_recordings:
            raise Exception
        #
        html_recordings += '<div class="row">'
        html_recordings += '<div class="col-xs-10"><h5>Title</h5></div>'
        html_recordings += '<div class="col-xs-2" style="text-align: right;"><h5>#</h5></div>'
        html_recordings += '</div>'
        #
        folderCount = 0
        while folderCount < len(json_recordings['recordings']):
            #
            iFolder = json_recordings['recordings'][str(folderCount)]
            seriesdrop_html = ''
            #
            itemCount = 0
            while itemCount < len(iFolder['items']):
                #
                iFile = iFolder['items'][str(itemCount)]
                #
                if not iFile['episodeNumber']['series'] == '' and not iFile['episodeNumber']['episode'] == '':
                    episodenumber = 'Series {se} Episode {ep}'.format(se=iFile['episodeNumber']['series'],
                                                                      ep=iFile['episodeNumber']['episode'])
                else:
                    episodenumber = ''
                #
                imgFile = get_image(iFile['channel']['id'], iFile['channel']['quality'], iFile['channel']['plus1'])
                img = '<img style="height: 25px;" src="/img/channel/{imgFile}"/>'.format(imgFile=imgFile)
                #
                seriesdrop_html += '<div class="row">'
                seriesdrop_html += '<div class="col-xs-9"><h5>{ep_title}</h5></div>'.format(ep_title=iFile['episodeTitle'])
                seriesdrop_html += '<div class="col-xs-3" style="text-align: right;">{img}</div>'.format(img=img)
                seriesdrop_html += '</div>'
                seriesdrop_html += '<div class="row"><div class="col-xs-12"><p>{desc}</p></div></div>'.format(desc=iFile['description'])
                seriesdrop_html += '<div class="row" style="margin-bottom: 20px">'
                seriesdrop_html += '<div class="col-xs-6"><p>{episodenumber}</p></div>'.format(episodenumber=episodenumber)
                seriesdrop_html += '<div class="col-xs-6" align="right"><p>{date}</p></div>'.format(date=iFile['recordingDate'])
                seriesdrop_html += '</div>'
                #
                itemCount += 1
            #
            html_recordings += '<div class="row btn-col-grey btn_pointer" style="margin-bottom: 5px;" data-toggle="collapse" data-target="#collapse_series{count}">'.format(count=folderCount)
            #
            # Based Bootstrap's Scaffolding (12-column grid)
            # | (9) Title | (2) Number of episodes | (1) Movie/TV Image |
            # | (9) Episode title | (3) Channel logo |
            # | (12) Description |
            # | (6) Series & Episode number | (6) Recording date |
            #
            html_recordings += '<div class="col-xs-9"><h5>{title}</h5></div>'.format(title=iFolder['folderName'])
            #
            if iFolder['type']=='tv':
                html_recordings += '<div class="col-xs-2" style="text-align: right;"><h6>{count}</h6></div>'.format(count=len(iFolder['items']))
            else:
                html_recordings += '<div class="col-xs-2" style="text-align: right;"></div>'
            #
            if iFolder['type']=='tv' or iFolder['type']=='movie':
                html_recordings += '<div class="col-xs-1" style="text-align: right; padding: 5px;"><img style="height: 25px;" src="/img/icon/ic_{type}.png"/></div>'.format(type=iFolder['type'])
            else:
                html_recordings += '<div class="col-xs-1" style="text-align: right;"></div>'
            #
            html_recordings += '</div>'
            html_recordings += '<div class="row collapse out" id="collapse_series{count}"><div class="container-fluid">{drop}</div></div>'.format(count=folderCount,
                                                                                                                                                  drop=seriesdrop_html)
            #
            folderCount += 1
            #
        return html_recordings
    except Exception as e:
        log_internal(logException, logDesc__vironmedia_tivo__CreateRecordings, exception=e)
        return '<p>Error</p>'


def _get_recordings(service):
    #
    host = 'http://{ip}:{port}'.format(ip=service['ip'],
                                       port=service['port'])
    uri = service_uri_virginmediativo_recordings
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get('{host}{uri}'.format(host=host, uri=uri), headers=headers)
    #
    logResult = logPass if (r.status_code == requests.codes.ok) else logFail
    log_outbound(logResult,
                 service['ip'], service['port'], 'GET', uri,
                 '-', '-',
                 r.status_code)
    #
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False


def _get_channels(service):
    #
    host = 'http://{ip}:{port}'.format(ip=service['ip'],
                                       port=service['port'])
    uri = service_uri_virginmediativo_channels
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get('{host}{uri}'.format(host=host, uri=uri), headers=headers)
    #
    logResult = logPass if (r.status_code == requests.codes.ok) else logFail
    log_outbound(logResult,
                 service['ip'], service['port'], 'GET', uri,
                 '-', '-',
                 r.status_code)
    #
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False


def _get_current_chan(service):
    #
    host = 'http://{ip}:{port}'.format(ip=service['ip'],
                                       port=service['port'])
    uri = service_uri_virginmediativo_channel
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get('{host}{uri}'.format(host=host, uri=uri), headers=headers)
    #
    logResult = logPass if (r.status_code == requests.codes.ok) else logFail
    log_outbound(logResult,
                 service['ip'], service['port'], 'GET', uri,
                 '-', '-',
                 r.status_code)
    #
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False
