 let viewproduct =$(".view-product")



//  smooth scroll on reload 
window.onload = function () {
    
    
    $("body").animate({'scrollTop':viewproduct.offset().top + 1},500)
   
    

 }



      
let selectedImage= document.querySelector(".colors-product-images").children

for(var i=0; i<selectedImage.length - 1;i++){
    selectedImage[i].addEventListener('click',function(e){
        e.preventDefault();

        this.classList.add("selected-color")
        this.classList.add("slct")
 
        $(this).siblings().removeClass("selected-color")
        $(this).siblings().removeClass("slct")

        for(var kkkk= 0; kkkk<listswatches.length; kkkk++){
            if(this.dataset.color == thumnailimages[kkkk].dataset.color){
                thumnailimages[kkkk].click()
            }
        }
    })
}


let customSelect= document.querySelector(".custom-select").children
let addToCrtBtn= document.querySelector('.addToCart')
for(var i=0; i <= customSelect.length - 1 ;i++){
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
        $("body").animate({'scrollTop':productDetCont.offsetTop*1.178},800)
    }else{
        $("body").animate({'scrollTop':viewproduct.offset().top + 1},800)
    }
   
    
})






//on hover on th eimage 





let lens = document.getElementById("lens")


function ZoomImg(imgId){

    var img = document.getElementById(imgId)
    lens.style.backgroundImage = `url(${img.src})`
    let imgcont = document.getElementById("imgcontpro")
    
    let ratio = 2
    lens.style.backgroundSize = (img.width * ratio) + "px " + (img.height * ratio) + 'px' 
  

    
    imgcont.addEventListener('mouseleave',function(){
        lens.style.opacity = 0
        
    })
    
    img.addEventListener('mousemove',function(e){
        lens.style.opacity = 1
        var bounds = img.getBoundingClientRect()

        
        var x = e.pageX - bounds.left
        var y = e.pageY - bounds.top

        var posleft =     x - (lens.offsetWidth / 2 )
        var postop = y - (lens.offsetHeight / 2 )

       
        if(posleft < 0){
            posleft =0
        }
        if(postop < 0){
            postop =0
        }


        lens.style.left =   posleft + "px"
        lens.style.top =  postop + "px"
        lens.style.backgroundPosition = '-' + (x * ratio) + 'px -' + (y * ratio) + 'px'
        
    })
    lens.addEventListener('mousemove',function(e){
        lens.style.opacity = 1
        var bounds = img.getBoundingClientRect()
        var x = e.pageX - bounds.left
        var y = e.pageY - bounds.top

        x = x - window.pageXOffset
        y = y - window.pageYOffset

        var posleft = x - (lens.offsetWidth / 2 )
        var postop = y - (lens.offsetHeight / 2 )

        if(posleft < 0){
            posleft =0
        }
        if(postop < 0){
            postop =0
        }

        lens.style.left =   posleft + "px"
        lens.style.top =  postop + "px"
        lens.style.backgroundPosition = '-' + (x * ratio) + 'px -' + (y * ratio) + 'px'
        
    })
   
}



ZoomImg("imgprod")



//change background of scatches availebale colors for the product

var listswatches = document.querySelectorAll(".swatches .select-table")

for(var listI=0; listI< listswatches.length; listI++){
    var color = listswatches[listI].dataset.color

    listswatches[listI].style.backgroundColor = color
}

var colorsvalues= document.querySelectorAll(".colorsvalues .selected-value ")
var targeted= colorsvalues[colorsvalues.length - 1]
var replacedvalue = targeted.textContent.replace('/','')
targeted.textContent = replacedvalue



//thumbnail images width ajust
var thumnailcont=document.querySelector('.thumbnail-images');
var thumnailimages=document.querySelectorAll('.thumbnail-images .img')
var mainImg=document.getElementById('imgprod')
var lensback= document.getElementById('lens')

thumnailcont.style.width = thumnailimages.length*60

for(var k=0; k< thumnailimages.length;k++){
    thumnailimages[k].addEventListener('click',function(e){
        var imgthumbsrc=this.childNodes[0].src
        this.classList.add('selected')
        $(this).siblings().removeClass("selected")
        
        mainImg.src = imgthumbsrc
        mainImg.parentNode.href=imgthumbsrc
        
        lens.style.backgroundImage = `url(${imgthumbsrc})`
        for(var kkk= 0; kkk<listswatches.length; kkk++){
            if(this.dataset.color == listswatches[kkk].dataset.color){
                listswatches[kkk].click()
            }
        }
      
    })
}



function wishlistApi(id, action){
    url="/wishlistApi/"
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "productId":id,
            "action":action,
            
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        //
            location.reload()
        
       

        //
    })
}

var wishlistBtn = document.getElementById("wishbtn")

wishlistBtn.addEventListener("click",function(){

    this.classList.toggle("added")
    var wishproduct=this.dataset.product 

    if(this.classList.contains('added')){
      

        // this.innerHTML = `<i class="fas fa-heart"></i> Remove From WishList`
        wishlistApi(wishproduct,"add")

    }else{
        
        // this.innerHTML = `<i class="far fa-heart"></i> Add To WishList`
        wishlistApi(wishproduct,"remove")

    }

    

    
})


var btnload = document.getElementById("btnload");


btnload.addEventListener("click",function(){
    
    //
    var lengthproducts = document.getElementById("productidcontainer").childElementCount - 1;
    

    var catrgoryrelated = this.dataset.category;
    
   this.dataset.rows=parseInt(this.dataset.rows)+1
   
    var rowsnumber = this.dataset.rows
    
    loadrelated(rowsnumber, catrgoryrelated, lengthproducts, this)
    
    
});



//function of making an api and use it though
function loadrelated(id,cat,sliceno, clickedbtn){
    url="/rows/"
    
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "rows":id,
            "cat":cat,
            "slice":sliceno,
           
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((product)=>{

        if(product.all == "yes"){
            clickedbtn.remove()
        }

        document.getElementById("productidcontainer").innerHTML=''
        //
        

     
        // location.reload()
        for(var i=0;i<product.data.length;i++){
            var val=0
            var newpricepromo= product.data[i].new_price
            var oldpricepromo= product.data[i].old_price
            var promotion=(parseInt(newpricepromo) / parseInt(oldpricepromo))*100
            if(promotion.toString().split('').length >= 2){
                val= promotion.toString().split('').slice(0,2).join('')
                           }

            
                       
            document.getElementById("productidcontainer").innerHTML +=`
           
            <div class="product">
            <a href='/product/${product.data[i].id}/'>
            ${
                product.data[i].is_promotion?
                   `<div id="promo${product.data[i].id}spv" class="promotion">`
                       +  val +'%' +
                   `</div>`
                
            :
            ''
        }
                <div class="productImg">
                    <img class="skeleton" src=" ${product.data[i].image}" alt="">
                </div>
            </a>
                
                <div class="productDescription">
                    <div class="productName skeleton-text">
                        <h5>${ product.data[i].name }</h5>
                    </div>
                    <div class="productPrice">
                        <div class="through skeleton-text">
                            ${ product.data[i].old_price <=0 ? 
                            `<p>Free</p>`
                            : 
                            `<p>${product.data[i].old_price}$</p>`
                            }
                                
                            
                        </div>
                        <div  class="realPrice skeleton-text">
                            <h5>${ product.data[i].new_price <= 0? 
                                `Free`
                                : 
                                `${product.data[i].new_price}$`
                                }</h5>
                        </div>
                    </div>
                    <div class="rate">
                    ${product.data[i].rate == 0?
                    `<i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 0.5?

                    `<i class="fas fa-star-half-alt"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 1?
                        
                    `<i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 1.5?
                    
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 2?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 2.5?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 3?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 3.5?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 4?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 4.5?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 5?
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>`
                    :
                    product.data[i].rate == 5.5?
                    ` <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star-half-alt"></i>`                     
                    :
                    `<i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>`
                    }
                    </div>
                    <div class="btns">
                        <button data-product='${product.data[i].id}' data-action='add'  class="addToCart">Add to cart</button>
                        
                    </div>
                    </div>
                    
            </div>
        `

        }

       

        //
    })
}


