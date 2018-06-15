import os
import requests
from resources.global_resources.variables import *
from resources.global_resources.log_vars import logPass, logFail
from log.log import log_outbound


def createPage_nest(service):
    #
    data = _get_nest_data(service)
    #
    btn_count = 0
    btn_count += 1 if len(data['thermostats']) else 0
    btn_count += 1 if len(data['smoke_co_alarms']) else 0
    btn_count += 1 if len(data['cameras']) else 0
    btn_width = int(12 / btn_count)
    #
    btn_first = True
    #
    resources = '<script src="/resource/js/jarvis.service_page.nest.js"></script>'
    resources += '<link rel="stylesheet" href="/resource/css/jarvis.service_page.nest.css">'
    resources += '<script>setInterval(updatePage({service_id}), 30000);</script>'.format(service_id=service['service_id'])
    #
    html_buttons = ''
    html_body = ''
    #
    # thermostats
    if len(data['thermostats']):
        if btn_first:
            cls_active = '_active'
            btn_first = False
        else:
            cls_active = ''
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
            html_buttons += f.read().format(width=btn_width,
                                            service_id=service['service_id'],
                                            function_id='thermostats',
                                            function_name='Thermostats',
                                            btn_class='service_function_btn{active}'.format(active=cls_active))
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
            html_body += f.read().format(service_id=service['service_id'],
                                         function_id='thermostats',
                                         function_body=_html_thermostats(service['service_id'], data['thermostats']),
                                         body_class='service_function_body{active}'.format(active=cls_active))
    #
    # smoke_co_alarms
    if len(data['smoke_co_alarms']):
        if btn_first:
            cls_active = '_active'
            btn_first = False
        else:
            cls_active = ''
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
            html_buttons += f.read().format(width=btn_width,
                                            service_id=service['service_id'],
                                            function_id='smoke_co_alarms',
                                            function_name='Smoke Alarms',
                                            btn_class='service_function_btn{active}'.format(active=cls_active))
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
            html_body += f.read().format(service_id=service['service_id'],
                                         function_id='smoke_co_alarms',
                                         function_body=_html_smokes(service['service_id'], data['smoke_co_alarms']),
                                         body_class='service_function_body{active}'.format(active=cls_active))
    #
    # cameras
    if len(data['cameras']):
        if btn_first:
            cls_active = '_active'
            btn_first = False
        else:
            cls_active = ''
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_btn.html'), 'r') as f:
            html_buttons += f.read().format(width=btn_width,
                                            service_id=service['service_id'],
                                            function_id='cameras',
                                            function_name='Cameras',
                                            btn_class='service_function_btn{active}'.format(active=cls_active))
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/service_function_body.html'), 'r') as f:
            html_body += f.read().format(service_id=service['service_id'],
                                         function_id='cameras',
                                         function_body=_html_cameras(service['service_id'], data['cameras']),
                                         body_class='service_function_body{active}'.format(active=cls_active))
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


def _get_nest_data(service):
    #
    service_url = 'http://{ip}:{port}{uri}'.format(ip=service['ip'],
                                                   port=service['port'],
                                                   uri=service_uri_nest_data_all)
    #
    headers = {service_header_clientid_label: serviceId}
    r = requests.get(service_url, headers=headers)
    #
    if r.status_code == requests.codes.ok:
        log_outbound(logPass,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_apps_all,
                     '-', '-',
                     r.status_code)
        return r.json()
    else:
        log_outbound(logFail,
                     service['ip'], service['port'], 'GET', service_uri_lgtvnetcast_apps_all,
                     '-', '-',
                     r.status_code)
        return False


def _html_thermostats(service_id, data):
    #
    _html = ''
    count = 0
    #
    for thermostat_id in data:
        thermostat = data[thermostat_id]
        #
        device_id = thermostat['device_id']
        therm_name = thermostat['name']
        #
        if thermostat['is_online']:
            #
            is_online = 'online'
            #
            therm_hvac_state = thermostat['hvac_state']
            if therm_hvac_state == 'heating':
                temp_hvac_statement = 'Heating to'
            elif therm_hvac_state =='cooling':
                temp_hvac_statement = 'Cooling to'
            else:
                temp_hvac_statement = 'Heat set to'
            #
            _temp_unit = thermostat['temperature_scale'].lower()
            temp_unit_html = '&#8451;' if _temp_unit == 'c' else '&#8457'
            therm_temp_target = thermostat['target_temperature_{unit}'.format(unit=_temp_unit)]
            therm_temp_ambient = thermostat['ambient_temperature_{unit}'.format(unit=_temp_unit)]
            #
            therm_label = 'Current: '
            #
            new_temp_up = therm_temp_target + 0.5
            new_temp_down = therm_temp_target - 0.5
            #
            therm_leaf = thermostat['has_leaf']
            #
        else:
            #
            is_online = 'offline'
            therm_hvac_state = 'offline'
            temp_hvac_statement = ''
            _temp_unit = ''
            temp_unit_html = ''
            therm_label = 'Offline'
            therm_temp_target = ''
            therm_temp_ambient = ''
            therm_leaf = 'false'
            new_temp_up = ''
            new_temp_down = ''
        #
        remaining = len(data) - count
        if remaining == 1:
            colwidth = '12'
        elif remaining == 2:
            colwidth = '6'
        elif remaining == 3:
            colwidth = '4'
        else:
            colwidth = '3'
        #
        args = {'colwidth': colwidth,
                'service_id': service_id,
                'nest_device_id': device_id,
                'name': therm_name,
                'therm_label': therm_label,
                'is_online': is_online,
                'temp_hvac': temp_hvac_statement,
                'temp_target': therm_temp_target,
                'temp_ambient': therm_temp_ambient,
                'temp_unit': _temp_unit,
                'temp_unit_symbol': temp_unit_html,
                'has_leaf': str(therm_leaf).lower(),
                'hvac': therm_hvac_state,
                'new_temp_up': new_temp_up,
                'new_temp_down': new_temp_down}
        #
        if count > 0 and count % 4 == 0:
            _html += '</div><div class="row">'
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/nest/thermostat.html'), 'r') as f:
            _html += f.read().format(**args)
        #
        # UI ticks only created for celsius
        if _temp_unit == 'c':
            #
            _str_to_replace = 'tick-target temp-tick-c-{temp}'.format(temp=therm_temp_target)
            _html = _html.replace(_str_to_replace, 'tick-target tick-target-active')
            #
            if therm_hvac_state == 'heating' or therm_hvac_state == 'cooling':
                _str_to_replace = 'tick-ambient temp-tick-c-{temp}'.format(temp=therm_temp_ambient)
                if therm_temp_ambient < therm_temp_target:
                    _col = 'blue'
                else:
                    _col = 'red'
                _html = _html.replace(_str_to_replace, 'tick-ambient tick-ambient-active tick-ambient-active-{col}'.format(col=_col))
            #
            _str_to_replace = 'tick-target temp-tick-c-{temp}'.format(temp=therm_temp_target)
            _html = _html.replace(_str_to_replace, 'tick-target tick-target-active')
            #
            if therm_hvac_state == 'heating' or therm_hvac_state =='cooling':
                _str_to_replace = 'tick-ambient temp-tick-c-{temp}'.format(temp=therm_temp_ambient)
                if therm_temp_ambient < therm_temp_target:
                    _col = 'blue'
                else:
                    _col = 'red'
                _html = _html.replace(_str_to_replace, 'tick-ambient tick-ambient-active tick-ambient-active-{col}'.format(col=_col))
            #
        #
        count += 1
        #
    #
    return _html


def _html_smokes(service_id, data):
    #
    _html = ''
    count = 0
    #
    for smoke_id in data:
        smoke = data[smoke_id]
        #
        device_id = smoke['device_id']
        smoke_name = smoke['name']
        #
        if smoke['is_online']:
            smoke_online = 'online'
            battery_health = smoke['battery_health']  # ok / replace
            co_alarm_state = smoke['co_alarm_state']  # ok / warning / emergency
            smoke_alarm_state = smoke['smoke_alarm_state']  # ok / warning / emergency
            ui_color_state = smoke['ui_color_state']  # gray / green / yellow / red
        else:
            smoke_online = 'offline'
            battery_health = ''
            co_alarm_state = ''
            smoke_alarm_state = ''
            ui_color_state = ''
        #
        remaining = len(data) - count
        if remaining == 1:
            colwidth = '12'
        elif remaining == 2:
            colwidth = '6'
        elif remaining == 3:
            colwidth = '4'
        else:
            colwidth = '3'
        #
        args = {'colwidth': colwidth,
                'service_id': service_id,
                'name': smoke_name,
                'online': smoke_online,
                'ui_color_state': ui_color_state,
                'battery_health': battery_health,
                'co_alarm_state': co_alarm_state,
                'smoke_alarm_state': smoke_alarm_state}
        #
        if count > 0 and count % 4 == 0:
            _html += '</div><div class="row">'
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/nest/smoke_co_alarm.html'), 'r') as f:
            _html += f.read().format(**args)
        #
        count += 1
        #
    #
    return _html


def _html_cameras(service_id, data):
    #
    _html = ''
    count = 0
    #
    for camera_id in data:
        camera = data[camera_id]
        #
        device_id = camera['device_id']
        cam_name = camera['name']
        #
        if camera['is_online']:
            cam_online = 'Online'
            img_color = 'blue'
            cam_streaming = camera['is_streaming']
        else:
            cam_online = 'Offline'
            img_color = 'gray'
            cam_streaming = ''
        #
        remaining = len(data) - count
        if remaining == 1:
            colwidth = '12'
        elif remaining == 2:
            colwidth = '6'
        elif remaining == 3:
            colwidth = '4'
        else:
            colwidth = '3'
        #
        args = {'colwidth': colwidth,
                'service_id': service_id,
                'color': img_color,
                'online': cam_online}
        #
        if count > 0 and count % 4 == 0:
            _html += '</div><div class="row">'
        #
        with open(os.path.join(os.path.dirname(__file__), '../../resources/html/services/nest/camera.html'), 'r') as f:
            _html += f.read().format(**args)
        #
        count += 1
        #
    #
    return _html
