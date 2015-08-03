
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

