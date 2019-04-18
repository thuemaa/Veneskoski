$(document).ready(function() {

    /*hide the navbar*/
    if ( window.innerWidth <= 1080) {
        $(".nav_links_container").hide();
        console.log("navcont hide");

        /*Hide mobile navbar on scroll*/
        var prevScrollpos = window.pageYOffset;
        $(window).scroll(function() {
            var scrollPos = window.pageYOffset;
            if (prevScrollpos > scrollPos) {
                $(".navbar").css('top',  "0");
                $(".nav_links_container").css('left',  "0");
            }
            else {
                $(".navbar").css('top',  "-9rem");
                $(".nav_links_container").css('left',  "-200px");
            }
            prevScrollpos = scrollPos;
            console.log(prevScrollpos + " cur pos: " + scrollPos);
        });
    }

    /*Show navbar when resizing from mobile to desktop*/
    $(window).resize(function() {
       if (window.innerWidth > 1080) $(".nav_links_container").show();
    });

    /*hide the inner links*/
    $("#ajankohtaista_div").hide();
    $("#tapahtumat_div").hide();

    /*set the click function for nav bar etc*/
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
        $(this).attr("class", "image_div_mouseover");
    });


    $(".image_div").mouseout(function() {
        $(this).attr("class", "image_div");
    });

    $(".market_div").mouseover(function() {
        $(this).toggleClass("market_div_mouseover");
    });

    $(".market_div").mouseout(function() {
        $(this).attr("class", "market_div");
    });

    /*/AJAX image handling, not in use
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

        $(".large_image_background").show();
    });

    $(".close_image_icon").click(function() {
        console.log("painoit tästä: " + $(this).find("img").attr("id") );
        $(".large_image_background").toggle();
    }); */

    $(document).mouseup(function(e)
    {
        var img_div = $(".large_image_div").find("img");
        if (!img_div.is(e.target) && img_div.has(e.target).length === 0)
        {
            $(".large_image_background").hide();
        }
    });

    /*removes width and height attributes from tinymce images*/
    tinydiv = $(".tinymce_div").find("img");
    console.log(tinydiv);

    tinydiv.each(function() {
        this.removeAttribute("width");
        this.removeAttribute("height");
        console.log(this);
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
