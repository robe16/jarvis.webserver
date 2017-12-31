function tvlgnetcast_updateScreenshot(service_id) {
    newSrc = "/service/image/" + service_id + "/screenshot?time=" + new Date().getTime()
    document.getElementById(service_id + "_screenshot").src = newSrc;
}


function tvlgnetcast_touch_mouseMove(service_id) {
    //
    var last_x
    var last_y
    //
    try {
        //
        while(MouseEvent.which==1) {
            //
            trackpad_id = "trackpad-" + service_id;
            var trackpad_obj = document.getElementById(trackpad_id);
            //
            current_x = instanceOfMouseEvent.clientX;
            current_y = instanceOfMouseEvent.clientY;
            //
            deltaX = last_x - current_x;
            deltaY = last_y - current_y;
            //
            sendCommand(service_id, {command: 'touchMove', touchMoveX: touchX, touchMoveY: touchY});
            //
            last_x = current_x;
            last_y = current_y;
            //
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}



function tvlgnetcast_touchMove(service_id) {
    //
    var last_x
    var last_y
    //
    try {
        //
        while(MouseEvent.which==1) {
            //
            trackpad_id = "trackpad-" + service_id;
            var trackpad_obj = document.getElementById(trackpad_id);
            //
            current_x = instanceOfMouseEvent.clientX;
            current_y = instanceOfMouseEvent.clientY;
            //
            deltaX = last_x - current_x;
            deltaY = last_y - current_y;
            //
            sendCommand(service_id, {command: 'touchMove', touchMoveX: touchX, touchMoveY: touchY});
            //
            last_x = current_x;
            last_y = current_y;
            //
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}