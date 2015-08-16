$(window).scroll(function(){
    if($(this).scrollTop() > 50)
    {   
        $(".navbar").addClass('navbar-inverse');
        $(".header").addClass('header-inverse');
    }else{
		$(".navbar").removeClass('navbar-inverse');
		$(".header").removeClass('header-inverse');
	}
});

$('#post-message').on('submit', function(event){
	event.preventDefault();
	post_message();
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function post_message(){
	var csrftoken = getCookie('csrftoken');
	$('.errorlist').each(function(i,ul){
		$(this).empty();
	});
	
	$.ajax({
		url:'/',
		type: 'POST',
		data:$('#post-message').serialize(),
		cache:false,
		beforeSend: function(xhr, settings) {
			$("#submit").html("Submit <i class=\"fa fa-spinner fa-pulse\"></i>");
        	if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        	    xhr.setRequestHeader("X-CSRFToken", csrftoken);
        	}
    	},
		success: function(json){
			$name=$('#id_name').val();
			$('#id_name').val('');
			$('#id_email').val('');
			$('#id_message').val('');
			
			if(json['errors']){
				$.each(json['errors'],function(key,errors){
					$ul=$('#'+key+'_error');
					$.each(errors,function(index,error){
						$ul.append("<li><i class=\"fa fa-asterisk\"></i> "+error);
					});
				});
			}else{
				$('#msg').html("<div class=\"alert alert-success\">Thank You "+$name+", we have received your message and will respond as required.</div>");
				grecaptcha.reset();
			}
			$("#submit").html("Submit");
		},
		error: function(xhr,errmsg,err){
			$('#msg').html("<div class=\"alert alert-danger\">Something wrong in form</div>");
			$("#submit").html("Submit");
		}
	});
	
	
}

