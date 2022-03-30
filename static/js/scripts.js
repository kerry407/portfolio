

  document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
          document.getElementById('home-nav').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.navbar').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
          document.getElementById('home-nav').style.boxShadow = "0px 5px 5px -3px rgb(0 0 0 / 10%)";
        } else {
          document.getElementById('home-nav').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
          document.getElementById('home-nav').style.boxShadow = "0px 0px 0px 0px";
        } 
    });
  }); 
  // DOMContentLoaded  end
  