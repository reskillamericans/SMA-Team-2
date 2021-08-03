document.addEventListener("DOMContentLoaded", () => {
    const register = document.getElementById("register");
    const bg = document.getElementById("bg-img");
    const confirmAccount = document.getElementById("accountConfirmed");
    const form = document.getElementById("registration-form");
    const userName = document.getElementById("user_name");
    const email = document.getElementById("user_email");
    const pwd = document.getElementById("user_password");
    const BtnSignup = document.getElementById("sign-up");


    confirmAccount.style.display ="none";
    



    form.addEventListener('input', function(e) {
        BtnSignup.addEventListener('click', function(e) {
            e.preventDefault();
        }); 
        if(userName.value !== "" && email.validity.valid && pwd.validity.valid) {
            BtnSignup.style.backgroundColor = "#9E8BC7";
            BtnSignup.addEventListener('click', showConfirmed);  
        } else{ 
            BtnSignup.style.backgroundColor = "#CCCCCC";
        };
    });

    function showConfirmed(){
        register.style.display = "none";
        confirmAccount.style.display = "block";
    };
    

    
    
});    