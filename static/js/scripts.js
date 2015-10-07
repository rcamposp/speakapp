$(document).ready(function() {
  $('#sidr-button').sidr({
  	onOpen : function() {
			$('.sidr-overlay').show();
		}
  });

  $('body').on('click', '.sidr-overlay', function(){
		$.sidr('close', 'sidr');
		$(this).hide();
	});
});