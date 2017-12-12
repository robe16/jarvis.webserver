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
        xhr.send(dataJSON);
        //
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}