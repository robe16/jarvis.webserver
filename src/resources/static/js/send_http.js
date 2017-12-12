function getHttp(url, alert, return_rsp_string, callback_lvl2) {
    //
    alert = alert || false;
    return_rsp_string = return_rsp_string || false;
    callback_lvl2 = callback_lvl2 || false;
    //
    try {
        var xmlHttp = commonHttp(url, "GET", alert, null, callback_lvl2);
    } catch(err) {
        alertTrigger(false);
        return false;
    }
}

function postHttp(url, alert, payload, callback_lvl2) {
    //
    alert = alert || false;
    payload = payload || null;
    callback_lvl2 = callback_lvl2 || false;
    //
    try {
        var xmlHttp = commonHttp(url, "POST", alert, payload, callback_lvl2);
    } catch(err) {
        alertTrigger(false);
        return false;
    }
}

function deleteHttp(url, alert, callback_lvl2) {
    //
    alert = alert || false;
    callback_lvl2 = callback_lvl2 || false;
    //
    try {
        commonHttp(url, "DELETE", alert, null, callback_lvl2);
    } catch(err) {
        alertTrigger(false);
        return false;
    }
}

function httpCallback(xhr, alert, return_rsp_string, callback_lvl2) {
    if (xhr == true) {
        //
        if (alert) {alertTrigger(xhr.status==200);}
        //
        if (return_rsp_string) {
            var rsp = xmlHttp.responseText;
        } else {
            var rsp = (xhr.status==200);
        }
        //
        if (callback_lvl2) {callback_lvl2(rsp);}
        //
    }
}


function alertTrigger(success) {
    if (success) {
        var v = document.getElementById('cmd_success')
    } else {
        var v = document.getElementById('cmd_fail')
    }
    v.style.display="block";
    setTimeout(function(){v.style.display="none"}, 2000);
}


function commonHttp(url, method, alert, return_rsp_string, payload, callback_lvl2) {
    //
    alert = alert || false;
    return_rsp_string = return_rsp_string || false;
    payload = payload || null;
    callback_lvl2 = callback_lvl2 || false;
    //
    var xhr = new XMLHttpRequest();
    //
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            httpCallback(xhr, alert, return_rsp_string, callback_lvl2);
        }
    };
    xhr.onerror = function () {
        console.error(xhr.statusText);
        httpCallback(false);
    };
    //
    xhr.open(method, url, true); // true = async
    xhr.send(payload);
}





function sendHttp(url, data, method, responserequired, alert) {
    //
    url = url || "/";
    data = data || "/";
    method = method || "GET"; // Assume 'get' if not defined
    responserequired = responserequired || 0
    alert = alert || false
    //
    // responserequired:
    // 0 = none
    // 1 = text/body of response
    // 2 = success/failure boolean
    try {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open(method, url, false);
        xmlHttp.send(data);
        if (alert){
            if (xmlHttp.status==200){
                var v = document.getElementById('cmd_success')
            } else {
                var v = document.getElementById('cmd_fail')
            }
            v.style.display="block";
            setTimeout(function(){v.style.display="none"}, 2000);
        }
        if (responserequired == 0) {
            return;
        } else if (responserequired == 1) {
            if (xmlHttp.status==200) {return xmlHttp.responseText;} else {return false;}
        } else if (responserequired == 2) {
            if (xmlHttp.status==200) {return true;} else {return false;}
        }
    }
    catch(err) {
        var v = document.getElementById('cmd_fail')
        v.style.display="block";
        setTimeout(function(){v.style.display="none"}, 2000);
        if (responserequired) {return false;}
    }
}