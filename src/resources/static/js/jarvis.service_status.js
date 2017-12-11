function removeService(serviceID) {
    try {
        // Confirmation box
        r = confirm("You are about to remove service '" + serviceID + "'\n\nThe service will only be added again to the list of available services once re-discovered by the web server.\n\nAre you sure?");
        //
        if (r == true){
            //
            var url = '/services/remove/' + serviceID
            //
            success = deleteHttp(url=url, alert=false, callback=removeService_callback)
            //
            if (success == true) {
                alert("Service " + serviceID + "has been removed and will only be added to list of available services once re-discovered.")
            }
            //
        } else {
            //
            alert("Action cancelled\n\nService " + serviceID + "has not been removed.")
            //
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}

function removeService_callback(success) {
    try {
        if (success == true) {
            alert("Service " + serviceID + "has been removed and will only be added to list of available services once re-discovered.")
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}