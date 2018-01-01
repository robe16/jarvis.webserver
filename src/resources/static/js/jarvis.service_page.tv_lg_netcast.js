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
    var mouseMoveFlag = false;
    var mouseAllowClick = true;
    //
    var waitTime = 100; // 0.1sec
    //
    //
    trackpad_obj.addEventListener('touchstart', function(e) {
        //
        sendCommand(service_id, {command: 'cursorVisbility', visibility: true});
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
        if (mouseMoveFlag) {
            //
            var touchobj = e.changedTouches[0]
            //
            var current_x = parseInt(touchobj.clientX);
            var current_y = parseInt(touchobj.clientY);
            //
            var deltaX = current_x - last_x;
            var deltaY = current_y - last_y;
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
    trackpad_obj.addEventListener('touchend', function(e) {
        //
        setTimeout(allow_click, 10);     // 0.01 seconds
        setTimeout(cursor_hide, 10000);  // 10 seconds
        //
    }, false)
    //
    // TODO - touch version of 'click'
    //
    //
    trackpad_obj.addEventListener('mousedown', function(e) {
        //
        mouseMoveFlag = true;
        mouseAllowClick = false;
        //
        sendCommand(service_id, {command: 'cursorVisbility', visibility: true});
        //
        last_x = parseInt(e.clientX);
        last_y = parseInt(e.clientY);
        //
    }, false)
    //
    trackpad_obj.addEventListener('mousemove', function(e) {
        //
        if (mouseMoveFlag) {
            //
            var current_x = parseInt(e.clientX);
            var current_y = parseInt(e.clientY);
            //
            var deltaX = current_x - last_x;
            var deltaY = current_y - last_y;
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
        mouseMoveFlag = false;
        //
        setTimeout(allow_click, 10);     // 0.01 seconds
        setTimeout(cursor_hide, 10000);  // 10 seconds
        //
    }, false)
    //
    trackpad_obj.addEventListener('click', function(e) {
        //
        if (mouseAllowClick) {
            sendCommand(service_id, {command: 'touchClick'});
        }
        //
    }, false)
    //
    //
    //
    //
    function allow_click() {
        mouseAllowClick = true;
    }
    //
    function cursor_hide() {
        if (!mouseMoveFlag) {
            sendCommand(service_id, {command: 'cursorVisbility', visibility: false});
        }
    }
    //
    //
}