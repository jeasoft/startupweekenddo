/* Project specific Javascript goes here. */


$(document).ready (function () {

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
    
    //vertical hack:
    verticalAlignHack('#coaches .row .col-sm-8, #coaches .row .col-sm-4');
    
    function verticalAlignHack( elements ) {
        $( elements ).each(function() {
            var ph = $(this).parent().height();
            var h = $(this).height();
            
            $(this).css({
                position: 'relative',
                top: ph / 2 - h / 2
            });
        });
    }

});
