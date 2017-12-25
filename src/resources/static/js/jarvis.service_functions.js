function changeFunction(service_id, service_function) {

    var function_id_start = "service-function-"

    var function_body_id_start = function_id_start + "body-" + service_id + "-"
    var function_body_id = function_body_id_start + service_function

    var button_button_id_start = function_id_start + "btn-" + service_id + "-"
    var button_button_id = button_button_id_start + service_function

    var all = document.getElementsByTagName("div");

    for (var i = 0; i < all.length; i++) {

        if (all[i].id.startsWith(function_id_start)) {

            if (all[i].id.startsWith(function_body_id_start)) {
                if (all[i].id==function_body_id) {
                    document.getElementById(all[i].id).classList.add("service_function_body_active");
                } else {
                    document.getElementById(all[i].id).classList.remove("service_function_body_active");
                };
            };
            if (all[i].id.startsWith(button_button_id_start)) {
                if (all[i].id==button_button_id) {
                    document.getElementById(all[i].id).classList.add("service_function_btn_active");
                } else {
                    document.getElementById(all[i].id).classList.remove("service_function_btn_active");
                };
            };

        };

    };
}
