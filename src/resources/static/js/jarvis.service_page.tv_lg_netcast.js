function tvlgnetcast_updateScreenshot(service_id) {
    newSrc = "/service/image/" + service_id + "/screenshot?time=" + new Date().getTime()
    document.getElementById(service_id + "_screenshot").src = newSrc;
}


function tvlgnetcast_touchpad(service_id) {
    //
    var trackpad_id = "trackpad-" + service_id;
    var trackpad_obj = document.getElementById(trackpad_id);
    //
    var last_x;
    var last_y;
    //
    var waitTime = 500; // 0.5sec
    //
    // http://www.javascriptkit.com/javatutors/touchevents.shtml
    //
    trackpad_obj.addEventListener('touchstart', function(e) {
        //
        var touchobj = e.changedTouches[0]
        //
        last_x = parseInt(touchobj.clientX);
        last_y = parseInt(touchobj.clientY);
        //
    }, false)
    //
    trackpad_obj.addEventListener('touchmove', function(e) {
        //
        var touchobj = e.changedTouches[0]
        //
        var current_x = parseInt(touchobj.clientX);
        var current_y = parseInt(touchobj.clientY);
        //
        var deltaX = last_x - current_x;
        var deltaY = last_y - current_y;
        //
        sendCommand(service_id, {command: 'touchMove', touchMoveX: deltaX, touchMoveY: deltaY});
        //
        last_x = current_x;
        last_y = current_y;
        //
        wait(waitTime);
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
    trackpad_obj.addEventListener('mousedown', function(e) {
        //
        sendCommand(service_id, {command: 'cursorVisbility', visibility: true});
        mouseDownFlag = true;
        //
    }, false)
    //
    trackpad_obj.addEventListener('mousemove', function(e) {
        //
        if (mouseDownFlag) {
            //
            last_x = parseInt(e.clientX);
            last_y = parseInt(e.clientY);
            //
            wait(waitTime);
            //
            var current_x = parseInt(e.clientX);
            var current_y = parseInt(e.clientY);
            //
            var deltaX = last_x - current_x;
            var deltaY = last_y - current_y;
            //
            sendCommand(service_id, {command: 'touchMove', touchMoveX: deltaX, touchMoveY: deltaY});
            //
            last_x = current_x;
            last_y = current_y;
            //
            wait(waitTime);
            //
        }
        //
    }, false)
    //
    trackpad_obj.addEventListener('mouseup', function(e) {
        //
        mouseDownFlag = false;
        setTimeout(cursor_hide, 2000);
        //
    }, false)
    //
    //
    function cursor_hide() {
        //
        if (!mouseDownFlag) {
            sendCommand(service_id, {command: 'cursorVisbility', visibility: false});
        }
        //
    }
    //
    //
}