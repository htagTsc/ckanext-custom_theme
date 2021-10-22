ckan.module('recent-datasets-carousel', function ($) {    
    return {
      initialize: function () {        
        var $carousel = $("#recent-datasets-carousel", this.element);
        var $items = $(".carousel-inner .item", this.element);        
        var $indicators = $(".carousel-indicators li", this.element);

        $carousel.on('slide.bs.carousel', function(e){        
          var ai = $items.closest(".active").index();
          $indicators.removeClass("active");          
          $indicators.eq(ai).toggleClass("active");                  
        });
      }
    };
  });