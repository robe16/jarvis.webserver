function sendNest_thermostat_tempUp(service_id, device_id) {
    //
    var temp_unit = _nest_thermostat_temp_unit(device_id);
    var temp_target_current = _nest_thermostat_temp_target_current(device_id, temp_unit);
    var temp_increment = _nest_thermostat_temp_increment(temp_unit);
    //
    var temp_target_new = temp_target_current + temp_increment;
    //
    sendNest_thermostat_temp(service_id, device_id, temp_target_new, temp_unit);
    setTimeout(updatePage(service_id), 2000);
    //
}

function sendNest_thermostat_tempDown(service_id, device_id) {
    //
    var temp_unit = _nest_thermostat_temp_unit(device_id);
    var temp_target_current = _nest_thermostat_temp_target_current(device_id, temp_unit);
    var temp_increment = _nest_thermostat_temp_increment(temp_unit);
    //
    var temp_target_new = temp_target_current - temp_increment;
    //
    sendNest_thermostat_temp(service_id, device_id, temp_target_new, temp_unit);
    setTimeout(updatePage(service_id), 2000);
    //
}

function _nest_thermostat_temp_unit(device_id) {
    return document.getElementById(device_id + "_temp_unit").getAttribute("temp_unit");
}

function _nest_thermostat_temp_target_current(device_id, temp_unit) {
    var _temp = document.getElementById(device_id + "_temp_target").innerHTML;
    //
    if (temp_unit=="c") {
        return parseFloat(_temp);
    } else {
        return parseInt(_temp);
    }
}

function _nest_thermostat_temp_increment(temp_unit) {
    if (temp_unit=="c") {
        return 0.5;
    } else {
        return 1;
    }
}

function sendNest_thermostat_temp(service_id, device_id, new_temperature, temp_unit) {
    var cmd = {device_type: "thermostat",
               device_id: device_id};
    //
    if (temp_unit=="c") {
        cmd.target_temperature_c = new_temperature
    } else {
        cmd.target_temperature_f = new_temperature
    }
    //
    sendCommand(service_id, cmd);
}