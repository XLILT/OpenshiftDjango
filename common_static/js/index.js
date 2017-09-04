$(".nav.navbar-nav li").click(function() {
	if($(this).text() === "注册") {
		$(".form-registry").removeClass("hide");
		$(".form-signin").addClass("hide");
		$(".nav.navbar-nav li").removeClass("active");
		$(this).addClass("active");
	}
	else if($(this).text() === "登陆") {
		$(".form-signin").removeClass("hide");
		$(".form-registry").addClass("hide");
		$(".nav.navbar-nav li").removeClass("active");
		$(this).addClass("active");
	}
});

!function() {
}();
