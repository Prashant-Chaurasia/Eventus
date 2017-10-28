




var scrollSpeed = 10;
    
    // set the default position
    var current = 0;

    // set the direction
    var direction = 'v';

    function bgscroll(){

        // 1 pixel row at a time
        current -= 1;
   
        // move the background with backgrond-position css properties
        $('div.clouds').css("backgroundPosition", (direction == 'h') ? current+"px 0" : "0 " + current+"px");
   
    }

    //Calls the scrolling function repeatedly
     setInterval(bgscroll, scrollSpeed);    


	
$(".form")
  .find("input, textarea")
  .on("keyup blur focus", function(e) {
    var $this = $(this),
      label = $this.prev("label");

    if (e.type === "keyup") {
      if ($this.val() === "") {
        label.removeClass("active highlight");
      } else {
        label.addClass("active highlight");
      }
    } else if (e.type === "blur") {
      if ($this.val() === "") {
        label.removeClass("active highlight");
      } else {
        label.removeClass("highlight");
      }
    } else if (e.type === "focus") {
      if ($this.val() === "") {
        label.removeClass("highlight");
      } else if ($this.val() !== "") {
        label.addClass("highlight");
      }
    }
  });

$(".tab a").on("click", function(e) {
  e.preventDefault();

  $(this)
    .parent()
    .addClass("active");
  $(this)
    .parent()
    .siblings()
    .removeClass("active");

  target = $(this).attr("href");

  $(".tab-content > div")
    .not(target)
    .hide();

  $(target).fadeIn(600);
});

