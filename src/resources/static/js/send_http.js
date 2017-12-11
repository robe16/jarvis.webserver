function getHttp(url, alert) {
    //
    try {
        var xmlHttp = commonHttp(url=url, method="GET");
//        var xmlHttp = new XMLHttpRequest();
//        xmlHttp.open("GET", url, false);
//        xmlHttp.send(data);
        //
        if (alert) {alertTrigger(xmlHttp.status==200)}
        if (xmlHttp.status==200) {return xmlHttp.responseText;} else {return false;}
        //
    }
    catch(err) {
        alertTrigger(false);
        return false;
    }
}

function postHttp(url, alert, payload) {
    //
    try {
        var xmlHttp = commonHttp(url=url, method="POST", payload=payload);
        //
        if (alert) {alertTrigger(xmlHttp.status==200)}
        if (xmlHttp.status==200) {return true} else {return false;}
        //
    }
    catch(err) {
        alertTrigger(false);
        return false;
    }
}

function deleteHttp(url, alert) {
    //
    try {
        var xmlHttp = commonHttp(url=url, method="DELETE");
        //
        if (alert) {alertTrigger(xmlHttp.status==200)}
        if (xmlHttp.status==200) {return true} else {return false;}
        //
    }
    catch(err) {
        alertTrigger(false);
        return false;
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


function commonHttp(url, method, payload) {
    //
    payload = payload || null;
    //
    var xhr = new XMLHttpRequest();
    xhr.open(method, url, true); // true = async
    //
    xhr.onload = function (e) {
      if (xhr.readyState === 4) {
        return xhr;
      }
    };
    xhr.onerror = function (e) {
      console.error(xhr.statusText);
      return False
    };
    //
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