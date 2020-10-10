console.log(">> Script called for first time");

$(document).ready(function(){
	console.log('>> Form validation script started');

	// Email regex
	const emailRegex = /[a-zA-Z0-9]+@[a-zA-Z0-6]{2,}.(com|co|es|en|fr|it|pt|ir|bg|nl|no|au|ch|de|sw|gl|gal|int|org|edu)/

	// Password regex's
	const lowerCase = /[a-z]+/;
	const upperCase = /[A-Z]+/;
	const number = /[0-9]/;
	const special = /[$%@&*]/;
	const lettersReg = /[a-z]/mig;
	const lettersEntropy = Math.log2(26); console.log(lettersEntropy);
	const numberSpecialReg = /[0-9$@%&*]/mig;
	const numberSpecialEntropy = Math.log2(94); console.log(numberSpecialEntropy);

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
	
	// Set email validation
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

	password.each(function() {
		$(this).on('input', function() {
			console.log('Password changed')
			// Set drop password tips status
			console.log('Lower case: ' + lowerCase.test($(this).val()));
			let lowerCaseIcon = $(this).closest('.form-password--drop').children('pre').children('.lowercaseIcon');
			if (lowerCase.test($(this).val())) {
				lowerCaseIcon.attr('uk-icon', 'check');
			} else {
				lowercaseIcon.attr('uk-icon', 'close');
			}
			//_ = (lowerCase.test($(this).val())) ? lowerCaseIcon.attr('uk-icon', 'check') : lowercaseIcon.attr('uk-icon', 'close');
			upperCase.test($(this).val()) ? $(this).closest('.uppercaseIcon').attr('uk-icon', 'check') : $(this).closest('.uppercaseIcon').attr('uk-icon', 'close');
			number.test($(this).val()) ? $(this).closest('.numberIcon').attr('uk-icon', 'check') : $(this).closest('.numberIcon').attr('uk-icon', 'close');
			special.test($(this).val()) ? $(this).closest('.specialIcon').attr('uk-icon', 'check') : $(this).closest('.specialIcon').attr('uk-icon', 'close');
			// Record entropy points
			let points = 0;
			console.log(lettersReg.exec($(this).val()));
			if (lettersReg.exec($(this).val()) != null) {
				points += lettersReg.exec($(this).val()).length * lettersEntropy;
			}
			if (numberSpecialReg.exec($(this).val()) != null) {
				points += numberSpecialReg.exec($(this).val()).length * numberSpecialEntropy;
			}
			console.log('Password points: ' + points + ' (for password: ' + $(this).val() + ')');
			let progressBar = $(this).closest('.form-password--progress');
			if (points < 30) {
				progressBar.addClass('uk-text-danger');
				progressBar.attr('value', '1');
			} else if (points < 50) {
				progressBar.addClass('uk-text-warning');
				progressBar.attr('value', '2');
			} else if (points < 75) {
				progressBar.addClass('uk-tex-primary');
				progressBar.attr('value', '3');
			} else {
				progressBar.addClass('uk-text-success');
				progressBar.attr('value', '4');
			}
		})
	});

	console.log('>> Form validation script finished');
});

function passwordEntropy (password) {
	let letters = lettersReg.match(password) * lettersEntropy;
}