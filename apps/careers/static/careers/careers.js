(function($) {
    "use strict"

    
    var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();
    var burgerMenu = function() {

		$('.js-colorlib-nav-toggle').on('click', function(event){
			event.preventDefault();
			var $this = $(this);

			if ($('body').hasClass('offcanvas')) {
				$this.removeClass('active');
				$('body').removeClass('offcanvas');	
			} else {
				$this.addClass('active');
				$('body').addClass('offcanvas');	
			}
		});
	};
	burgerMenu();

	// Click outside of offcanvass
	var mobileMenuOutsideClick = function() {

		$(document).click(function (e) {
	    var container = $("#colorlib-aside, .js-colorlib-nav-toggle");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {

	    	if ( $('body').hasClass('offcanvas') ) {

    			$('body').removeClass('offcanvas');
    			$('.js-colorlib-nav-toggle').removeClass('active');
			
	    	}
	    	
	    }
		});

		$(window).scroll(function(){
			if ( $('body').hasClass('offcanvas') ) {

    			$('body').removeClass('offcanvas');
    			$('.js-colorlib-nav-toggle').removeClass('active');
			
	    	}
		});

	};
	mobileMenuOutsideClick();

	function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
	const csrftoken = getCookie('csrftoken');
	console.log(csrftoken);
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    var send_data = {}
    $('#location').on('change', function () {
        if(this.value == "all")
            send_data['location'] = "";
        else
            send_data['location'] = this.value;
        getAPIData();
    });
    $('#category').on('change', function () {
        if(this.value == "all")
            send_data['category'] = "";
        else
            send_data['category'] = this.value;
        getAPIData();
    });
    $('#jobtype').on('change', function () {
        // var favorite = [];
        var i=1;
        for(i=1;i<=5;i++){
            if ($("input[name='jobtype"+i+"']:checked")){
                send_data['jobtype'+i] = $("input[name='jobtype"+i+"']:checked").val();
            }else{
                send_data['jobtype'+i] = "";
            }
        }
        // send_data['jobtype'] = favorite;
        getAPIData()
    });
    
    function getAPIData() {
        $.ajax({
            url: "/careers/filter/",
            method: 'GET',
            data : send_data,
            success: function(data){
                console.log(data);
            },
            error: function(xhr, errmsg, err){
                console.log("error");
            }
        });
    }
    $('#save').click(function(){
        $.ajax({
            type: "POST",
            url: $("#like").attr('action'),
            data: $("#like").serialize(),
            error: function (xhr, status, error) {
                    if(xhr.status=="403"){
                        window.location.href = "/login/";
                    }
                },
            success: function(response) {
                //success message mybe...
                
                if (response['is_liked']) {
                    var count = $( "#likes_count" ).val();
					count += 1;
                    $("#save").html('<i class="fa fa-heart"></i>');
                    $("#likes_count").text(count);
                } 
                if (!response['is_liked'])  {
                    
                    $("#save").html('<i class="fa ti-heart"></i>');
                    var newcount = $( "#likes_count" ).val();
                    $("#likes_count").text(newcount);
                    
                    
                }
            }
        });

    });

    
    
})(jQuery);
var send_data = {}

