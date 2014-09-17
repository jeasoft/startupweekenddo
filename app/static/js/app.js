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

	$("#more-button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#home-navbar").offset().top
	   		}, 1000);
		});

	$('#nav-wrapper').height($("#home-navbar").height());
    
    $('#home-navbar').affix({
        offset: { top: $('#home-navbar').offset().top }
    });

});
