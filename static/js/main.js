$(document).ready(function() {
	//http://www.eyecon.ro/bootstrap-datepicker/
	//http://stackoverflow.com/questions/18887950/how-do-i-get-bootstrap-datepicker-to-work-with-bootstrap-3
	$('.input-group.date').datepicker({
	    format: "yyyy-mm-dd",
	    autoclose: true, 
	    todayHighlight: true 
	});
	$('.input-group.date > .form-control').attr('readonly', '');



	//repeat table header
	
	
	var h = $('table thead');
	var td = $('table tbody tr').eq(0);
	td.children().each(function(index, el) {
		var elem = $(this);
		var width = elem.outerWidth();
		elem.css({'width': width});
	});
	var w = $(document);
	h.children().children().each(function(index, el) {
		var elem = $(this);
		var width = elem.outerWidth();
		elem.css({'width': width});
	});

	var top = h.offset().top;
	$(window).scroll(function() {
		
		if(top<w.scrollTop()){
			h.addClass('abs');
		}
		else {
			h.removeClass('abs');
		}
	});
});