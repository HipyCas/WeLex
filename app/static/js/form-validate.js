console.log(">> Script called for first time");

$(document).ready(function(){
	console.log('>> Form validation script started');

	// Create regex's
	const emailRegex = /[a-zA-Z0-9]+@[a-zA-Z0-6]{2,}.(com|co|es|en|fr|it|pt|ir|bg|nl|no|au|ch|de|sw|gl|gal|int|org|edu)/

	// Get form components
	console.log("> Getting elements");
	const required = $(".form-required"); console.log("required: " + required);
	const password = $(".form-password"); console.log("Password: " + password);
	const email = $(".form-email"); console.log("Email: " + email);
    const submit = $(".form-submit"); console.log("Submit: " + submit);

    // Create vars to record state
    console.log("> Setting valid vars");
    var requiredValid = (required.length > 0) ? false : true; console.log("required Valid: " + requiredValid);
    var passwordValid = (password.length > 0) ? false : true; console.log("Password Valid:" + passwordValid);
    var emailValid = (email.length > 0) ? false : true; console.log("Email Valid: " + emailValid);

    // Disable button until all conditions are met
    console.log("> Disabling submit button");
    submit.attr("disabled", "true");

    // Add '*' to required fields
    required.each(function() {
    	$(this).attr(
    	"placeholder",
    	$(this).attr("placeholder") + " *");
	})

    // Set no-empty validation
    required.each(function() {
    	$(this).on('input', function(event) {
    		if ($(this).val().length < 1) {  // Case length is smaller than 0, meaning field is empty
    			$(this).addClass('uk-form-danger');
    			$(this).attr('uk-tooltip', 'This field is required');
				UIkit.tooltip($(this)).show();
    		} else {
    			$(this).removeClass('uk-form-danger');
    			$(this).removeAttr('uk-tooltip');
			}
			// Determine if all .form-required are valid
    		let allValid = true;
    		required.each(function() {
    			if ($(this).val().length < 1)
    				allValid = false;
			});
    		requiredValid = allValid; // set global requiredValid to allValid so others can know if .form-required are completed
    		if (requiredValid && passwordValid && emailValid) { // Check length of password an email items so you're not always comparing to a false
    			submit.removeAttr('disabled');  // Enable button
    		}
    	});
	});
	
	email.each(function() {
		$(this).on('input', function(event) {
			if (!emailRegex.test($(this).val())) {
				$(this).addClass('uk-form-danger');
				$(this).attr('uk-tooltip', 'Not a valid email address');
				UIkit.tooltip($(this)).show();
			} else {
				$(this).removeClass('uk-form-danger');
				$(this).removeAttr('uk-tooltip');
			}
			let allValid = true;
			email.each(function() {
				if (!emailRegex.test($(this).val())) {
					allValid = false;
				}
			});
			emailValid = allValid;
			if (requiredValid && passwordValid && emailValid) {
				submit.removeAttr('disabled');
			}
		});
	});

	console.log('>> Form validation script finished');
});