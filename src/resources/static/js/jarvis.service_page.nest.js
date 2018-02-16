function sendNest_thermostat_tempUp(service_id, device_id) {
    //
    var tempCurrent = _nest_thermostat_temp_current(device_id);
    var tempNew = tempCurrent + 0.5;
    //
    sendNest_thermostat_temp(service_id, device_id, tempNew);
    setTimeout(updatePage(service_id), 2000);
    //
}

function sendNest_thermostat_tempDown(service_id, device_id) {
    //
    var tempCurrent = _nest_thermostat_temp_current(device_id);
    var tempNew = tempCurrent - 0.5;
    //
    sendNest_thermostat_temp(service_id, device_id, tempNew);
    setTimeout(updatePage(service_id), 2000);
    //
}

function _nest_thermostat_temp_current(device_id) {
    return document.getElementById(device_id + '_temp').innerHTML;
}

function sendNest_thermostat_temp(service_id, device_id, new_temperature) {
    sendCommand(service_id, {device_type: 'thermostat', device_id: device_id, temperature: new_temperature});
}