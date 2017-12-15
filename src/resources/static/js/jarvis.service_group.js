function switchService(service_id) {
    // Buttons
    //
    img_id = "grp_btn_" + service_id
    //
    var all = document.getElementsByTagName("img");
    for (var i = 0; i < all.length; i++) {
        if (all[i].id==(img_id)) {
            document.getElementById(all[i].id).classList.remove("grayscale");
        }
        else if (all[i].id.startsWith('grp_btn_')) {
            document.getElementById(all[i].id).classList.add("grayscale");
        };
    };
    //
    // Body
    //
    div_id = "grp_body_" + service_id
    var all = document.getElementsByTagName("div");
    for (var i = 0; i < all.length; i++) {
        if (all[i].id==(div_id)) {
            document.getElementById(all[i].id).classList.remove("grp_body_hide");
            document.getElementById(all[i].id).classList.add("grp_body_show");
        }
        else if (all[i].id.startsWith('grp_body_')) {
            document.getElementById(all[i].id).classList.remove("grp_body_show");
            document.getElementById(all[i].id).classList.add("grp_body_hide");
        };
    };
    //
}