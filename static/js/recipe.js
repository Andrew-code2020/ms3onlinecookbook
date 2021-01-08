$(document).ready(function(){
     /*--base template navbar--*/
     $(".sidenav").sidenav({edge: "right"});
     /*--register, edit profile, edit recipe page dropdown menu--*/
     $('select').formSelect();
     /*--collapsible in recipes--*/
    $('.collapsible').collapsible();
  });
       

  console.log('linked properly');


  