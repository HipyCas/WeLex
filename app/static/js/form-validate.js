console.log(">> Script called for first time");

$(document).ready(function(){
	console.log('>> Form validation script started');

	// Get form components
	console.log("> Getting elements");
	const required = $(".form-required"); console.log("required: " + required);
	const password = $(".form-password"); console.log("Password: " + password);
	const email = $(".form-email"); console.log("Email: " + email);
    const submit = $(".form-submit"); console.log("Submit: " + submit);

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
    		let valid = false;
    		if ($(this).val().length < 1) {
    			$(this).addClass('uk-form-danger');
    			$(this).attr('uk-tooltip', 'This field is required');
    			valid = false;
    		} else {
    			$(this).removeClass('uk-form-danger');
    			$(this).removeAttr('uk-tooltip');
    			valid = true;
    		}
    		let allValid = true;
    		required.each(function() {
    			if ($(this).val().length < 1)
    				allValid = false;
    		});
    		requiredValid = allValid;
    		if (requiredValid && passwordValid && emailValid) { // Chcek length of password an email items so you're not always comparing to a false
    			submit.removeClass('uk-disabled');
    		}
    	});
    });

	console.log('>> Form validation script finished');
});