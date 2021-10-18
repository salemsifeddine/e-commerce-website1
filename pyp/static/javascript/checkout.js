//check form infos

var email= document.getElementById("id_email")
var zip_code1= document.getElementById("zip")
var zip_code2= document.getElementById("zip2")
var address= document.getElementById("address")
var city= document.getElementById("city")
var state= document.getElementById("state")
var alertform = $("#messageform")

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
  }

buttonSubmitShip.addEventListener("click", function(e){
    var inputs = document.querySelectorAll(".shopping-info div input , .user-info  input ")

    

if(validateEmail(email.value) && address.value && city.value && state.value && zip_code1.value && zip_code2.value){
    
    
        ///
        if(prooved){
            $(this).show() 
            alertform.children("p").text("Exellent!!")
            alertform.css("background","#B1E693")
            alertform.animate({"left":0}, 700)
            setTimeout(() => {
                alertform.animate({"left":-190 + 'px'}, 1200)
            }, 2500);

        }else{
            e.preventDefault();
            document.getElementById("paypal-button-container").style.display = "block"
            $(this).hide() 
        }
        

   

}else{
    e.preventDefault()  
 
    for(var inp=0; inp <= inputs.length - 1; inp++){

        inputs[inp].style.background = 'rgba(199, 199, 252, 0.54)';
        inputs[inp].style.borderRadius = '2px';
        inputs[inp].style.border = '1px solid rgba(51, 51, 51, 0.2)';
        inputs[inp].disabled = false
    }
    $(this).show() 
     
    

    alertform.children("p").text("Please check your informations, then submit!")
    alertform.animate({"left":0}, 700)
    
    setTimeout(() => {
        alertform.animate({"left":-190 + 'px'}, 1200)
    }, 2000);


}



})










////////////

zip_code1.addEventListener('keyup',function(e){
        length = e.target.value.split("").length
        value = e.target.value.split("")[length - 1]
       

        if(isNaN(value)){
           
            e.target.value = ""
          
        }
})

zip_code2.addEventListener('keyup',function(e){
    length = e.target.value.split("").length
    value = e.target.value.split("")[length - 1]
   

    if(isNaN(value)){
       
        e.target.value = ""
      
    }
})




////////////////

