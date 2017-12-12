function removeService(serviceID) {
    try {
        // Confirmation box
        r = confirm("You are about to remove service '" + serviceID + "'\n\nThe service will only be added again to the list of available services once re-discovered by the web server.\n\nAre you sure?");
        //
        if (r == true){
            //
            var url = '/services/remove/' + serviceID
            //
            var xhr = new XMLHttpRequest();
            //
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    removeService_callback(xhr.status==200, serviceID);
                }
            };
            xhr.onerror = function () {
                console.error(xhr.statusText);
                removeService_callback(false, serviceID);
            };
            //
            xhr.open("DELETE", url, true);
            xhr.send();
            //
        } else {
            //
            alert("Action cancelled\n\nService '" + serviceID + "' has not been removed.")
            //
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}

function removeService_callback(success, serviceID) {
    try {
        if (success == true) {
            alert("Service '" + serviceID + "' has been removed and will only be added to list of available services once re-discovered.")
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}