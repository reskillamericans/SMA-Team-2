document.addEventListener("DOMContentLoaded", () => {

    // header elements
    const LinkHome = document.getElementById("home");
    const LinkLoginPg = document.getElementById("login-pg");
    const LinkRegPg = document.getElementById("registration-pg");


    const landing = document.getElementById("landing");
    const loginForm = document.getElementById("login_form")
    const mail = document.getElementById("email");
    const password = document.getElementById("password");
    const BtnLogin = document.getElementById("btn-login");
    const BtnCreate = document.getElementById("btn-create");


    // registration page
    const register = document.getElementById("register");
    const BtnReg = document.getElementById("registrationClose");
    
    const form = document.getElementById("registration-form");
    const username = document.getElementById("username");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const BtnSignup = document.getElementById("sign-up");
    const age = document.getElementById("user_age");
    const BtnOk = document.getElementById("acc-ok");

    // Account Confirmed Success
    const confirmAccount = document.getElementById("accountConfirmed");
     // HEADER LINKS - SOME WILL CLEAR FORM
    // Link to landing page
    LinkHome.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkHome.addEventListener('click', showLanding);
    

    // Link to login page will clear the login form
    LinkLoginPg.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkLoginPg.addEventListener('click', showLanding);

    // Link to register page will clear the reg form 
    LinkRegPg.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkRegPg.addEventListener('click', showRegister);




    // X button on Registration Page to return to landing Page
    // Close Popups and Return to Landing Page
    BtnReg.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    BtnReg.addEventListener('click', showLanding);
    function showLanding(){
        landing.style.display = "block";
        confirmAccount.style.display = "none";
        register.style.display = "none";
        landing.style.display = "block";
       
    };

    // Testing function to see is user can login in and successfully
    function goodLogin(){
        BtnLogin.style.backgroundColor = "#9E8BC7";   
    };
      
    BtnLogin.addEventListener('click', function(e) {
        e.preventDefault();
        if(mail.validity.valid && password.validity.valid) {
            goodLogin();   
        };
    });  


    // If user wishes to create an account
    BtnCreate.addEventListener('click', showRegister);
    function showRegister(){
        register.style.display = "block";
        landing.style.display = "none";
        confirmAccount.style.display = "none";
    };
    form.addEventListener('input', changeColor);
        
    function changeColor() {
        if(username.value !==''){
            BtnSignup.style.backgroundColor = "#9E8BC7";  
        };
    };
    BtnSignup.addEventListener('click', function(e) {
        e.preventDefault();
    
    });
    BtnSignup.addEventListener('click', showConfirmed);  
    

    function showConfirmed(){
        register.style.display = "none";
        confirmAccount.style.display = "block";
        landing.style.display = "none";
       
    };

    // Return to the Landing Page
    BtnOk.addEventListener('click', showLanding);
});
