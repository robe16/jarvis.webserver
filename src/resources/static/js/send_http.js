function alertTrigger(success) {
    if (success) {
        var v = document.getElementById('cmd_success')
    } else {
        var v = document.getElementById('cmd_fail')
    }
    v.style.display="block";
    setTimeout(function(){v.style.display="none"}, 2000);
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
        if (alert){alertTrigger(xmlHttp.status==200);}
        if (responserequired == 0) {
            return;
        } else if (responserequired == 1) {
            if (xmlHttp.status==200) {return xmlHttp.responseText;} else {return false;}
        } else if (responserequired == 2) {
            if (xmlHttp.status==200) {return true;} else {return false;}
        }
    }
    catch(err) {
        alertTrigger(false);
        if (responserequired) {return false;}
    }
}