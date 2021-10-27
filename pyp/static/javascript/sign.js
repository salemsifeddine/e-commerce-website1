var buttonSignup = document.querySelector(".not-selected-sign")
var buttonSignin = document.querySelector(".selected-sign")
var signinCont = document.querySelector(".signinCont");
var signupCont = document.querySelector(".signupCont")

buttonSignup.addEventListener("click",function(){
  
    if(this.classList.contains("not-selected-sign") ){
        this.classList.remove("not-selected-sign");
        buttonSignin.classList.remove('selected-sign');
        this.classList.add("selected-sign");
        buttonSignin.classList.add('not-selected-sign');
        signinCont.style.display = "none"
        signupCont.style.display = "block"
    }else{
        
        
        buttonSignin.classList.remove('selected-sign');
        
        buttonSignin.classList.add('not-selected-sign');
        
    }


})