
$(document).ready(function() {
  if($(".toolkit-slider").length>0){
    //$(".toolkit-slider").hide();
  }
});

$(window).load(function() {
  if($(".toolkit-slider").length>0){
    if(Galleria){
     
      Galleria.loadTheme('themes/classic/galleria.classic.js');
      $(".toolkit-slider").css("height", "300px");

      Galleria.run('.toolkit-slider', {
        dataConfig: function(img) {
          return {
            title: $(img).attr('alt'),
            description: $(img).siblings('.description').html()
          };
        },
        lightbox: false,
        responsive:true,
        showInfo:true,
        _toggleInfo:false,
        transition:"fadeslide",
        transitionSpeed:"1000",
        thumbCrop:"height",
        carousel:false,
        thumbnails: "empty",
        showCounter:false
        
      });

    }
    else{
      
    }
  }
});