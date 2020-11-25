$(document).ready(function () {
    $("#header_btn").on("click", function () {
        $("#mobile_div_hide").removeClass("mobile-none");
        $("#overlay_header").removeClass("mobile-none")
        $("#mobile_div_hide").addClass("mobile-div");
        $("#overlay_header").addClass("overlay")
    });

    $("#overlay_header").on("click", function () {
        $("#mobile_div_hide").removeClass("mobile-div");
        $("#overlay_header").removeClass("overlay")
        $("#mobile_div_hide").addClass("mobile-none");
        $("#overlay_header").addClass("mobile-none")
    })

    if ($(".login_content").length) {
        $("#log_to_reg_btn").click(function () {
            $("#login_section").addClass("d-none");
            $("#register_section").removeClass("d-none");
        })

        $("#reg_to_log_btn").click(function () {
            $("#register_section").addClass("d-none");
            $("#login_section").removeClass("d-none");
        });
    }

    if($(".index-content").length){
        $("#userArea_item").addClass(' sidebar-item-active');
        $("#userArea_link").addClass('sidebar-link-active')
    }

    if($(".show-ticket-content").length || $(".write-ticket-content").length){
        $("#ticket_item").addClass(' sidebar-item-active');
        $("#ticket_link").addClass('sidebar-link-active')
    }
})