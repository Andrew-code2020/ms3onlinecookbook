$(document).ready(function(){
     /*--base template navbar--*/
     $(".sidenav").sidenav({edge: "right"});
     /*--register page dropdown menu--*/
     $('select').formSelect();
     /*--toggle in recipes--*/
     $( "." ).toggle();
  });
       

/*--Breakfast Lunch, Dinner and Snacks Recipes--*/

function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

/*--document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
  });--*/

  console.log('linked properly');

/*---top picture---*/

/*---middle picture 1---*/

/*---middle picture 2---*/
  
/*---bottom picture 1---*/
  