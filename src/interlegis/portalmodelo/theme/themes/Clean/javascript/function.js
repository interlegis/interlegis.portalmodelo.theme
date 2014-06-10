jQuery(document).ready(function(){
  
size = jQuery( document ).width();

if ( size < 749 ){

jQuery(".portletNavigationTree .portletItem").addClass("hiddenStructure");
jQuery('.portletNavigationTree .portletHeader').click(function(e){
e.preventDefault();
jQuery(".portletNavigationTree .portletItem").addClass("hiddenStructure");
jQuery(this).next().toggleClass("hiddenStructure");
});
}

});



