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

	console.log('>> Form validation script finished');
});