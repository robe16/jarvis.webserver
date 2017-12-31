function tvlgnetcast_updateScreenshot(service_id) {
    newSrc = "/service/image/" + service_id + "/screenshot?time=" + new Date().getTime()
    document.getElementById(service_id + "_screenshot").src = newSrc;
}

var tvlgnetcast_touch_flag = {};

function tvlgnetcast_touch_mouseMove(service_id) {
    //
    tvlgnetcast_touch_flag[service_id] = true;
    //
    var last_x = 0;
    var last_y = 0;
    var current_x = 0;
    var current_y = 0;
    var deltaX = 0;
    var deltaY = 0;
    //
    try {
        //
        while (tvlgnetcast_touch_flag[service_id]) {
            //
            var trackpad_id = "trackpad-" + service_id;
            // var trackpad_obj = document.getElementById(trackpad_id);
            //
            var offset = $("#" + trackpad_id).offset();
            $(document).mousemove(function(e){
                current_x = e.pageX - offset.left;
                current_y = e.pageY - offset.top;
            });
            //
            deltaX = last_x - current_x;
            deltaY = last_y - current_y;
            //
            sendCommand(service_id, {command: 'touchMove', touchMoveX: deltaX, touchMoveY: deltaY});
            //
            last_x = current_x;
            last_y = current_y;
            //
            wait(500); //0.5sec
            //
        }
    }
    catch(err) {
        alert("An error has been encountered, please try again.\n\n" + err)
    }
}


function tvlgnetcast_touch_mouseUp(service_id) {
    tvlgnetcast_touch_flag[service_id] = false;
}
