$(document).ready(function () {
    $(".nineteenthcentury").hide();
    $(".twentiethcentury").hide();
    $(".twentyfirstcentury").hide();
    $(".Dimensions").hide();
    $(".climate").hide();
    $(".wildanimals").hide();
    $(".gaa").hide();
    $(".soccer").hide();
    $(".rugby").hide();
    $(".music").hide();
    $(".language").hide();
    $(".science").hide();
});

/*----History-------------------------------------------------------------------*/
$(".toggleButton19").click(function (){
    $(".nineteenthcentury").toggle("slow");
});

$(".toggleButton20").click(function (){
    $(".twentiethcentury").toggle("slow");
}); 


$(".toggleButton21").click(function (){
    $(".twentyfirstcentury").toggle("slow");
});

/*-----Geography----------------------------------------------------------------------------------------------*/
$(".toggleButtonDimensions").click(function (){
    $(".Dimensions").toggle("slow");
});

$(".toggleButtonclimate").click(function (){
    $(".climate").toggle("slow");
});

$(".toggleButtonwildanimals").click(function (){
    $(".wildanimals").toggle("slow");
});

/*-----Sport----------------------------------------------------------------*/
$(".toggleButtongaa").click(function (){
    $(".gaa").toggle("slow");
});

$(".toggleButtonsoccer").click(function (){
    $(".soccer").toggle("slow");
});

$(".toggleButtonrugby").click(function (){
    $(".rugby").toggle("slow");
});


/*-----Culture----------------------------------------------------------------*/
$(".toggleButtonmusic").click(function (){
    $(".music").toggle("slow");
});

$(".toggleButtonlanguage").click(function (){
    $(".language").toggle("slow");
});

$(".toggleButtonscience").click(function (){
    $(".science").toggle("slow");
});
