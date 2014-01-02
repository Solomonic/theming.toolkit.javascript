function ClassicTheme(slider){
    /* make a decent content slider with nices effects*/
    console.log('<-- ClassicTheme -->');
    console.log(slider);
    if(Galleria){    
      Galleria.loadTheme('themes/classic/galleria.classic.js');
      $(".toolkit-slider-classic").css("height", "300px");

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
    
}

$(document).ready(function() {
  if($(".toolkit-slider").length>0){
    //$(".toolkit-slider").hide();
  }
});

$(window).load(function() {
  if($(".toolkit-slider-classic").length>0){
    try{
        ClassicTheme($(".toolkit-slider-classic"));    
    }
    catch(e){
        //error in classic theme
        console.log(e);
    }
    
  }

});