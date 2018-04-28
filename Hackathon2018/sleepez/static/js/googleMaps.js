$( document ).ready(function() {
    
    // alert( "ready!" );
    var $demo = $("#demo")
    function getLocation() {
        console.log("location");
          if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(showPosition);
              // console.log(navigator.geolocation.getCurrentPosition(showPosition));
          } else {
              $demo.html("Geolocation is not supported by this browser.");
          }
      }
    function showPosition(position) {
       $demo.html("Latitude: " + position.coords.latitude + 
      "<br>Longitude: " + position.coords.longitude); 
    }

    getLocation();


});
