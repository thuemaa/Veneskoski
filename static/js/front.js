$(document).ready(function() {

    /*hide the navbar*/
    $(".nav_links_container").hide();
    $("#ajankohtaista_div").hide();
    $("#tapahtumat_div").hide();
    /*set the click function for nav bar*/
    $("#navbutton").click(function() {
        toggleElement(this.id);
    });

    $("#ajankohtaista_a").click(function() {
        toggleElement(this.id);
    });

    $("#tapahtumat_a").click(function() {
        toggleElement(this.id);
    });
});

/*click function for toggling navbar elements*/
function toggleElement(id) {

    if (id == "navbutton") {
        /*hide extendable nav links on nav menu toggle*/
        $("#ajankohtaista_div").hide();
        $("#tapahtumat_div").hide();
        $("#ajankohtaista_a").parent().removeClass("active_link");
        $("#tapahtumat_a").parent().removeClass("active_link");

        $(".nav_links_container").toggle();

    }
    else if (id == "ajankohtaista_a") {
        $("#tapahtumat_div").hide();
        $("#tapahtumat_a").parent().removeClass("active_link");

        $("#ajankohtaista_div").toggle();
        /*change the background of active div*/
        $("#" + id).parent().toggleClass("active_link");
    }

    else {
        /*hide the other extendable menu and remove the active link class*/
        $("#ajankohtaista_div").hide();
        $("#ajankohtaista_a").parent().removeClass("active_link");

        $("#tapahtumat_div").toggle();
        $("#" + id).parent().toggleClass("active_link");
    }
}