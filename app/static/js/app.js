/* Project specific Javascript goes here. */


$(document).ready (function () {

	// Cover Full Screen

    $( "#cover" ).each(function(){
        var $this = $(this);
        $this.css({'min-height':($(window).height())+'px'});

        /*Recalculate on window resize*/
        $(window).resize(function(){
            $this.css({'min-height':($(window).height())+'px'});
        });
    });

    // Scroll Down Buttons

	$("#more-button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#home-navbar").offset().top
	   		}, 1000);
		});

    $("#acerca").click(function() {
        $('html, body').animate({
            scrollTop: $("#about").offset().top
            }, 1000);
        });

    $("#programa").click(function() {
        $('html, body').animate({
            scrollTop: $("#program").offset().top
            }, 1000);
        });

    $("#patrocinadores").click(function() {
        $('html, body').animate({
            scrollTop: $("#sponsors").offset().top
            }, 1000);
        });

    $("#colaboradores").click(function() {
        $('html, body').animate({
            scrollTop: $("#facilitator").offset().top
            }, 1000);
        });

    // Navbar affix

	$('#nav-wrapper').height($("#home-navbar").height());
    
    $('#home-navbar').affix({
        offset: { top: $('#home-navbar').offset().top }
    });

});
