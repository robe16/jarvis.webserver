function sendNestCmd(group, thing, command, value, nest_model, nest_device, nest_device_id) {
    //
    x = sendHttp('/command/' + group +
                '/' + thing +
                '?command=' + command +
                '&value=' + value +
                '&nest_model=' + nest_model +
                '&nest_device=' + nest_device +
                '&nest_device_id=' + nest_device_id, null, 'GET', 1, true)
    //
    if (x) {
        document.getElementById('body_nest').innerHTML = x;
    }
    //
}

function updateNest(url){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', url, false);
    xmlHttp.send(null);
    if (xmlHttp.status==200) {
        document.getElementById('body_nest').innerHTML = xmlHttp.responseText}
    setTimeout(function () {updateNest(url);}, 30000);
}