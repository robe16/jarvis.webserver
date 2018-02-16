function sendCommand(serviceID, data) {
    try {
        //
        var dataJSON = JSON.stringify(data);
        //
        var url = '/service/command/' + serviceID
        //
        var xhr = new XMLHttpRequest();
        //
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                alertTrigger(xhr.status==200);
            }
        };
        xhr.onerror = function () {
            console.error(xhr.statusText);
            alertTrigger(false);
        };
        //
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(dataJSON);
        //
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}

function updatePage(serviceID) {
    try {
        //
        var dataJSON = JSON.stringify(data);
        //
        var url = '/service/page/' + serviceID + '?body=True'
        //
        var xhr = new XMLHttpRequest();
        //
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                document.getElementById('page-body_' + serviceID).innerHTML = xhr.response;
            }
        };
        xhr.onerror = function () {
            console.error(xhr.statusText);
        };
        //
        xhr.open("GET", url, true);
        xhr.send();
        //
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}