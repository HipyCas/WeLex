console.log(">> Script called for first time");

$(document).ready(function(){
	console.log('>> Form validation script started');

	// Get form components
	console.log("> Getting elements");
	var required = $(".form-required"); console.log("required: " + required);
	var password = $(".form-password"); console.log("Password: " + password);
	var email = $(".form-email"); console.log("Email: " + email);
    var submit = $(".form-submit"); console.log("Submit: " + submit);

	console.log('>> Form validation script finished');
});