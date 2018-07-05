$(document).ready(function() {

    /*hide the navbar*/
    $(".nav_links_container").hide();
    /*set the click function for nav bar*/
    $("#navbutton").click(function() {
        toggleNav();
    });
});

/*hide responsive navbar on click*/
function toggleNav() {
    console.log("painettii nappia");
    $(".nav_links_container").toggle(500);
}