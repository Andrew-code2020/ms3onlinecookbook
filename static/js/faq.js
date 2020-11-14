$(document).ready(function () {
    $(".airports").hide();
    $(".transport").hide();
    $(".currency").hide();
    $(".activityhol").hide();
    $(".culturehol").hide();
    $(".wellnesshol").hide();
    $(".cityhol").hide();
});

/*--Travel--*/
$(".airports1").click(function() {
  $( ".airports" ).toggle( "slow", function() {
  });
});

/*---Transport---*/
$(".transport1").click(function() {
  $( ".transport" ).toggle( "slow", function() {
  });
});

/*---Currency---*/
$(".currency1").click(function() {
  $( ".currency" ).toggle( "slow", function() {
  });
});

/*---Activity---*/
$(".activityhol1").click(function() {
  $( ".activityhol" ).toggle( "slow", function() {
  });
});

/*----Culture---*/
$(".culturehol1").click(function() {
  $( ".culturehol").toggle( "slow", function() {
  });
});

/*---Wellness---*/
$(".wellnesshol1").click(function() {
  $(".wellnesshol").toggle( "slow", function() {
  });
});

/*---City Break---*/
$(".cityhol1").click(function() {
  $( ".cityhol").toggle( "slow", function() {
  });
});
