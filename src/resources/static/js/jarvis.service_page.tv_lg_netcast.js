function tvlgnetcast_updateScreenshot(service_id) {
    newSrc = "/service/image/" + service_id + "/screenshot?time=" + new Date().getTime()
    document.getElementById(service_id + "_screenshot").src = newSrc;
}


function tvlgnetcast_touchpad(service_id) {
    //
    var trackpad_id = "trackpad-" + service_id;
    var trackpad_obj = document.getElementById(trackpad_id);
    //
    var last_x = 0;
    var last_y = 0;
    //
    // http://www.javascriptkit.com/javatutors/touchevents.shtml
    //
    trackpad_obj.addEventListener('touchstart', function(e) {
        //
        last_x = parseInt(trackpad_obj.clientX);
        last_y = parseInt(trackpad_obj.clientY);
        //
    }, false)
    //
    trackpad_obj.addEventListener('touchmove', function(e) {
        //
        var current_x = parseInt(trackpad_obj.clientX);
        var current_y = parseInt(trackpad_obj.clientY);
        //
        var deltaX = last_x - current_x;
        var deltaY = last_y - current_y;
        //
        sendCommand(service_id, {command: 'touchMove', touchMoveX: deltaX, touchMoveY: deltaY});
        //
        last_x = current_x;
        last_y = current_y;
        //
        wait(500); //0.5sec
        //
    }, false)
    //
    trackpad_obj.addEventListener('touchend', function(e) {
        //
    }, false)
    //
    //
    var mouseDownFlag = false;
    //
    trackpad_obj.addEventListener('onmousedown', function(e) {
        //
        mouseDownFlag = true;
        //
        last_x = parseInt(trackpad_obj.clientX);
        last_y = parseInt(trackpad_obj.clientY);
        //
        wait(500); //0.5sec
        //
        while (mouseDownFlag) {
            //
            var current_x = parseInt(trackpad_obj.clientX);
            var current_y = parseInt(trackpad_obj.clientY);
            //
            var deltaX = last_x - current_x;
            var deltaY = last_y - current_y;
            //
            sendCommand(service_id, {command: 'touchMove', touchMoveX: deltaX, touchMoveY: deltaY});
            //
            last_x = current_x;
            last_y = current_y;
            //
            wait(500); //0.5sec
            //
        }
        //
    }, false)
    //
    trackpad_obj.addEventListener('onmouseup', function(e) {
        //
        mouseDownFlag = false;
        //
    }, false)
    //
    //
}