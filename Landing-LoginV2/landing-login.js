document.addEventListener("DOMContentLoaded", () => {

    // header elements
    const LinkHome = document.getElementById("home");
    const LinkLoginPg = document.getElementById("login-pg");
    const LinkRegPg = document.getElementById("registration-pg");


    const landing = document.getElementById("landing");
    const loginForm = document.getElementById("login-form")
    const mail = document.getElementById("email");
    const password = document.getElementById("password");
    const BtnLogin = document.getElementById("btn-login");
    const BtnCreate = document.getElementById("btn-create");


    // registration page
    const register = document.getElementById("register");
    const BtnReg = document.getElementById("registrationClose");
    
    const regForm = document.getElementById("registration-form");
    const username = document.getElementById("username");
    const fname = document.getElementById("first_name");
    const lname = document.getElementById("last_name");
    
    const email = document.getElementById("new_email");
    const n_password = document.getElementById("new_password");
    const c_password = document.getElementById("conf_password");
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
        // BtnLogin.style.backgroundColor = "#53B6E0"
       
    }); 
    LinkLoginPg.addEventListener('click', showLogin);
    

    // Link to register page will clear the reg form 
    LinkRegPg.addEventListener('click', function(e) {
        e.preventDefault();
    }); 
    LinkRegPg.addEventListener('click', showRegister);




    // X button on Registration Page to return to landing Page
    // Close Popups and Return to Landing Page
    
    BtnReg.addEventListener('click', showLanding);
    function showLanding(){
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
    BtnCreate.addEventListener('click', function(e) {
        e.preventDefault();
        if(mail.value == '' && password.value == '') {
            showRegister();   
        };
    });  
    
    function showRegister(){
        register.style.display = "block";
        landing.style.display = "none";
        confirmAccount.style.display = "none";
        if(landing.style.display = "none") {
            loginForm.reset();
        }; 
        
    };
    regForm.addEventListener('input', changeColor);
        
    function changeColor() {
        if(username.value !==''){
            BtnSignup.style.backgroundColor = "#9E8BC7";  
        };
    };
   
    BtnSignup.addEventListener('click', function(e) {
        e.preventDefault();
        if(username.value !=='' && fname.value !=='' && lname.value !=='' 
            && email.validity.valid && n_password.value == c_password.value && age.value >= 13) { 
            showConfirmed();
        };
    });
    
    function showConfirmed(){
        register.style.display = "none";
        confirmAccount.style.display = "block";
        landing.style.display = "none"; 
    };

    // Return to the Landing Page
    BtnOk.addEventListener('click', showLogin);
    function showLogin(){
        confirmAccount.style.display = "none";
        register.style.display = "none";
        landing.style.display = "block";
        if(register.style.display = "none") {
            form.reset();
        }; 
    };
});
