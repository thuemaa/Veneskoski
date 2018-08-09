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

    /*image mouseover funcs*/
    $(".image_div").mouseover(function() {
        //console.log("toimii");
        $(this).attr("class", "image_div_mouseover");
        //$(this).next().attr("class", "image_div_margin");
        //$(this).prev().attr("class", "image_div_margin");
        //$(".image_div").not(this).attr("class", "image_div_small");
    });


    $(".image_div").mouseout(function() {
        //console.log("toimii");
        $(this).attr("class", "image_div");
        //$(this).next().attr("class", "image_div");
        //$(this).prev().attr("class", "image_div");
        //$(".image_div").not(this).attr("class", "image_div");
    });

    //open the image
    $(".image_div").click(function() {
        console.log("painoit tästä: " + $(this).find("img").attr("id") );

        var image_pk = $(this).find("img").attr("id");

        $.ajax({
            url: '/ajax/image/',
            data: {
                'image_pk': image_pk
           },
            dataType: 'json',
            success: function(data) {
                $(".large_image_div").find("h2").text(data.otsikko);
                $(".large_image_div").find(".large_kuvaus").text(data.kuvaus);
                $(".large_image_div").find("img").attr("src", data.kuva);
            }
        });


        $(".large_image_background").toggle();
    });

    $(".close_image_icon").click(function() {
        console.log("painoit tästä: " + $(this).find("img").attr("id") );
        $(".large_image_background").toggle();
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