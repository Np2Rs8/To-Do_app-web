
function showPasswordLogin() {
    let btnShowPassword = document.getElementById('customCheck');
    let campPassword = document.querySelector('#password');

    if(btnShowPassword.checked) {
        campPassword.type = "text";
    } else {
        campPassword.type = "password";
    }
}


function showPasswordTemplate(password1, password2) {
    let btnShowPassword = document.getElementById('customCheck');
    let campPassword1 = document.querySelector(password1);
    let campPassword2 = document.querySelector(password2);

    if(btnShowPassword.checked) {
        campPassword1.type = "text";
        campPassword2.type = "text";
    } else {
        campPassword1.type = "password";
        campPassword2.type = "password";
    }
}


function showPasswordRegister() {
    showPasswordTemplate("#password1", "#password2");
}

function showPasswordResetConfirm() {
    showPasswordTemplate("#new_password1", "#new_password2");
}

