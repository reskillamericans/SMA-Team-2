document.addEventListener("DOMContentLoaded", () => {
    const landing = document.getElementById("landing");
    const loginForm = document.getElementById("login_form")
    const mail = document.getElementById("log_email");
    const password = document.getElementById("old_password");
    const BtnLogin = document.getElementById("btn-login");
    const create = document.querySelector(".create");
    const register = document.getElementById("register");
    const BtnReg = document.getElementById("registrationClose");
    const confirmAccount = document.getElementById("accountConfirmed");
    const form = document.getElementById("registration-form");
    const userName = document.getElementById("user_name");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const BtnSignup = document.getElementById("sign-up");
    const age = document.getElementById("user_age");
    const BtnOk = document.getElementById("acc-ok");
    
    // X button on Registration Page to return to landing Page
    BtnReg.addEventListener('click', showLanding);
    function showLanding(){
        register.style.display = "none";
        landing.style.display = "block";
    };

    // Testing function to see is user can login in and successfully
    function goodLogin(){
        landing.style.display = "none";
        confirmAccount.style.display ="block";
    };
    loginForm.addEventListener('input', function(e) {
        BtnLogin.addEventListener('click', function(e) {
            e.preventDefault();
        });    
        if(mail.validity.valid && password.validity.valid) {
            BtnLogin.addEventListener('click', goodLogin); 
            BtnLogin.style.backgroundColor = "#9E8BC7"; 
        };
    });


    // If user wishes to create an account
    create.addEventListener('click', showRegister);
    function showRegister(){
        register.style.display = "block";
        landing.style.display = "none";
    };

    // After registration, account is confirmed
    function showConfirmed(){
        register.style.display = "none";
        confirmAccount.style.display = "block";
    };
    
    form.addEventListener('input', function(e) {
        BtnSignup.addEventListener('click', function(e) {
            e.preventDefault();
        });    
        if(userName.value !== "" && email.validity.valid && pwd.validity.valid && age.value !== "") {
            BtnSignup.addEventListener('click', showConfirmed); 
            BtnSignup.style.backgroundColor = "#9E8BC7"; 
        };
    });

    // Return to the Landing Page
    BtnOk.addEventListener('click', showLogin);
    function showLogin(){
        confirmAccount.style.display = "none";
        landing.style.display = "block";
        BtnOk.style.backgroundColor = "#9E8BC7"; 
    };

    
    


});
