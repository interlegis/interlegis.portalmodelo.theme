$(document).ready(function() {
    //Set width for parliamentarian list item based on its image size.
    var parlamentarWidth = parseInt($('.tile-parlamentares img').attr('width'));
    $('.tile-parlamentares .list-item').css('width', parlamentarWidth/2 + parlamentarWidth);
});
