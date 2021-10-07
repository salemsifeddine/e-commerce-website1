 let secondnav =$(".secondnav")
//  smooth scroll on reload 




      
let selectedImage= document.querySelector(".colors-product-images").children

for(var i=0; i<selectedImage.length - 1;i++){
    selectedImage[i].addEventListener('click',function(e){
        e.preventDefault();

        this.classList.add("selected-color")
        this.classList.add("slct")
 
        $(this).siblings().removeClass("selected-color")
        $(this).siblings().removeClass("slct")
    })
}


let customSelect= document.querySelector(".custom-select").children
let addToCrtBtn= document.querySelector('.addToCart')
for(var i=0; i <= selectedImage.length ;i++){
    customSelect[i].addEventListener('click',function(e){
        e.preventDefault();

        if(! this.classList.contains('sizeDoesNotExist')){
            this.classList.add("active-size")
            $(this).siblings().removeClass("active-size");

            if(addToCrtBtn.classList.contains("disabled")){
                addToCrtBtn.classList.remove("disabled")
                addToCrtBtn.classList.add("active")
                
            }
            // data-action="add"
            addToCrtBtn.textContent = "add to cart"
            addToCrtBtn.setAttribute("data-action","add" )
        }
        
    })
}


let prodctDetScroll=document.querySelector('.product-detail-scroll')
let productDetCont=document.querySelector(".detail-info")
let afterpseudo=document.querySelector(".scrolled")

prodctDetScroll.addEventListener('click',function(){
    afterpseudo.classList.toggle("scrolled")
    if(!afterpseudo.classList.contains("scrolled")){
        $("body").animate({'scrollTop':productDetCont.offsetTop*1.255},800)
    }else{
        $("body").animate({'scrollTop':secondnav.offset().top + 1},800)
    }
   
    
})

//thumbnail images width ajust
var thumnailcont=document.querySelector('.thumbnail-images');
var thumnailimages=document.querySelectorAll('.thumbnail-images .img')

thumnailcont.style.width = thumnailimages.length*60

for(var k=0; k< thumnailimages.length;k++){
    thumnailimages[k].addEventListener('click',function(e){
        e.preventDefault();
        this.classList.add('selected')
        $(this).siblings().removeClass("selected")

    })
}

