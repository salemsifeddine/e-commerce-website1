

var buttons = document.getElementsByClassName("addToCart")
for(var i=0; i<buttons.length; i++){
    buttons[i].addEventListener("click",function(){
        
        id=this.dataset.product
        action=this.dataset.action
      
        if(user == "AnonymousUser"){
            // getCookieItem(id,action)
            
            var logauth = $('.logauth');
            logauth.fadeIn(500);
            
        }
        else{
            var selectQnt=''
            if(document.getElementById("quantity")){
                 selectQnt= document.getElementById("quantity")
                 quantity= selectQnt.value
            }else{
                quantity=1
            }
            
           //cal your api and five it the keys
           update(id,action,parseInt(quantity))
        
            
        }
    })
}


//make  a function and call it when user is not logges in
// function getCookieItem(id,action){
//     console.log(localStorage.setItem("quantity",23))
//     if(action == "add"){
//         if(localStorage.getItem("quantity") == undefined){
//             localStorage.setItem("quantity",1)
//             // cart[id] = {"quantity":1}

//         }else{
//             // cart[id]["quantity"] += 1
//             localStorage.setItem("quantity",localStorage.getItem('quantity') + 1 )
//         }
//     }
//     if(action=='remove'){
//         // cart[id][quantity] -=1;
//         localStorage.setItem("quantity",localStorage.getItem('quantity') - 1 )
//         if(localStorage.getItem('quantity') <= 0){
//             localStorage.removeItem('quantity')
//             // delete cart[id]
//         }
//     }

//     //update the cookie

//     // document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
    
//     // console.log(cart.Object.keys())
// }

//function of making an api and use it though
function update(id,action,qnt){
    url="/update/"
    
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "productId":id,
            "action":action,
            "quantity":qnt
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        //
        

        crt=document.getElementById("cartnum")
        location.reload()
        
       

        //
    })
}



//********** */
//change profile picture when user get uploaded his photo and before submit it

var concel = document.querySelector(".concel");
concel.addEventListener("click",function(){
    var logauth = $('.logauth');
    logauth.fadeOut(500);
})

var buttonSignup = document.querySelector(".not-selected-sign")
var buttonSignin = document.querySelector(".selected-sign")
var signinCont = document.querySelector(".signinCont");
var signupCont = document.querySelector(".signupCont")

buttonSignup.addEventListener("click",function(){
    console.log("dsqd")
   
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

buttonSignin.addEventListener("click",function(){
    
    if(this.classList.contains("not-selected-sign") ){
        this.classList.remove("not-selected-sign");
        buttonSignup.classList.remove('selected-sign');
        this.classList.add("selected-sign");
        buttonSignup.classList.add('not-selected-sign');
        signupCont.style.display = "none"
        signinCont.style.display = "block"
    }else{
        
        
        buttonSignup.classList.remove('selected-sign');
        
        buttonSignup.classList.add('not-selected-sign');
        
    }


})

var passwordthrough = document.querySelectorAll(".fa-eye-slash")
var passwordvue = document.querySelectorAll(".fa-eye")


passwordvue.forEach(ele=>{
    ele.addEventListener("click",function(){
      
            var inputpass = document.getElementById(this.dataset.id)
            inputpass.setAttribute("type","text")
                
            this.style.display = "none"
            var passeye = document.getElementById(this.dataset.sibl)
            passeye.style.display="block"
      
    })
})

passwordthrough.forEach(ele=>{
        ele.addEventListener('click',function(e){
        var inputpass = document.getElementById(this.dataset.id)
        console.log(inputpass)
        inputpass.setAttribute("type","password")
        this.style.display = "none"
        var passeye = document.getElementById(this.dataset.sibl)
        passeye.style.display="block"
    })
})




var signupbtn = document.getElementById("signup")
var signinbtn = document.getElementById("login")

signupbtn.addEventListener("click",function(e){
    e.preventDefault();
    if(user="anonymousUser"){
        var logauth = $('.logauth');
        logauth.fadeIn(500);
        buttonSignup.click()
    }
})
signinbtn.addEventListener("click",function(e){
    e.preventDefault();

    if(user="anonymousUser"){
        var logauth = $('.logauth');
        logauth.fadeIn(500);
        buttonSignin.click()
    }
})