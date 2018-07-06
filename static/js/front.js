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

/*click functions for toggling navbar elements*/
function toggleElement(id) {
    console.log("painettii nappia " + id);
    if (id == "navbutton") {
        $("#ajankohtaista_div").hide();
        $("#tapahtumat_div").hide();
        $(".nav_links_container").toggle();

    }
    else if (id == "ajankohtaista_a") {
        $("#tapahtumat_div").hide();
        $("#ajankohtaista_div").toggle();
        /*change the background of active div*/
        $("#" + id).parent().class("active_link");
        //$("#" + id).addClass("active_link");
        console.log( $("#ajankohtaista_a").parent() );
    }

    else {
        $("#ajankohtaista_div").hide();
        $("#tapahtumat_div").toggle();
    }
}