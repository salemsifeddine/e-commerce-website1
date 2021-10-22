var viewdeal= $("#viewdeal")

window.onload = function () {
    
    
    $("body").animate({'scrollTop':viewdeal.offset().top + 1},500)
   
    

 }


 var dealproductname = document.querySelector(".desc-t h1")
 var lengthname =dealproductname.textContent.trim().length

 if(lengthname >40 && lengthname <= 55){
    dealproductname.style.fontSize = 60
 }
 if(lengthname >55){
    dealproductname.style.fontSize = 40
 }
