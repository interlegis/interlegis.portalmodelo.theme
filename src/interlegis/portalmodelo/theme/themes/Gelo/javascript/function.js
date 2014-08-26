$(document).ready(function() {
    var $portletItem = $('.portletNavigationTree .portletItem'),
        $portletHeader = $('.portletNavigationTree .portletHeader');

    $(window).resize(function() {
        if ($(window).width() < 749) {
            $portletHeader.unbind();
            $portletItem.hide();
            $portletHeader.click(function(e) {
                e.preventDefault();
                $(this).next().slideToggle();
            });
        } else {
            $portletItem.show();
            $portletHeader.unbind();

        }
    }).resize();

});