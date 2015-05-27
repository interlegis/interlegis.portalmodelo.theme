$(document).ready(function() {
    var $portletItem = $(".portletNavigationTree .portletItem"),
        $portletHeader = $(".portletNavigationTree .portletHeader");

    //Injects mobile menu button
    $("header").append("<div class='menu-button'><button><span class='hiddenStructure'>Mostrar ou Ocultar Menu</span><i class='icon-reorder'></i></button></div>");

    //Show menu on mobile menu button click
    $(".menu-button button").on( "click", function() {
        $(this).toggleClass("menuAtivo");
        $portletItem.slideUp(200);
        $portletHeader.removeClass("menuAtivo");
        $("#column-one").slideToggle();

    });
    //Collapse menu according to screen size
    $(window).resize(function() {
        if ($(window).width() < 753) {
            $portletHeader.unbind();
            $(".menu-button button").removeClass("menuAtivo")
            $portletItem.hide();
            $("#column-one").hide();
            $("#column-one").addClass("menuAtivo");
            $portletHeader.click(function(e) {
                e.preventDefault();
                $(this).toggleClass("menuAtivo");
                $(this).next().slideToggle();
            });
        } else {
            $portletHeader.unbind();
            $portletItem.show();
            $("#column-one").removeClass("menuAtivo")
            $("#column-one").show();
            $(".menu-button button").removeClass("menuAtivo")
            $("#column-one").css("display","table-cell");
        }
    }).resize();


});
