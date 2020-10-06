console.log(">> Script called for first time");

$(document).ready(function(){
	console.log('>> Form validation script started');

	// Get form components
	console.log("> Getting elements");
	var required = $(".form-required"); console.log("required: " + required);
	var password = $(".form-password"); console.log("Password: " + password);
	var email = $(".form-email"); console.log("Email: " + email);
    var submit = $(".form-submit"); console.log("Submit: " + submit);

    // Create vars to record state
    console.log("> Setting valid vars");
    var requiredValid = false; console.log("required Valid: " + requiredValid);
    var passwordValid = false; console.log("Password Valid:" + passwordValid);
    var emailValid = false; console.log("Email Valid: " + emailValid);

    // Disable button until all conditions are met
    console.log("> Disabling submit button");
    submit.addClass("uk-disabled");

    // Add '*' to required fields
    required.each(function() {
    	$(this).attr(
    	"placeholder",
    	$(this).attr("placeholder") + " *");
    })

    // Set no-empty validation
    required.each(function() {
    	$(this).on('input', function(event) {
    		if ($(this).val().length < 1) {
    			$(this).addClass('uk-form-danger');
    			$(this).attr('uk-tooltip', 'This field is required');
    		} else {
    			$(this).removeClass('uk-form-danger');
    			$(this).removeAttr('uk-tooltip');
    		}
    	});
    });

	console.log('>> Form validation script finished');
});