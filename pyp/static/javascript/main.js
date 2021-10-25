

let catigoryelement = document.getElementsByClassName("category");
let selectedcatElement= document.getElementsByClassName('selectedCategory')
let hotdealdata;
var hotdealKey =0;




for(var i=0; i<catigoryelement.length;i++){
    catigoryelement[i].addEventListener('click',function(e){
       
        
       
        $(this).siblings('li').removeClass("selectedCategory")
        this.classList.add('selectedCategory');

        let categoryId = this.dataset.category;

        updateproducts(this.textContent,categoryId,this.dataset.section)
    })
}



//function hotdeals

function contentHotdeals(clicked,name,oldPrice,newPrice,imagesrc,link){

    let nameProductofTargeted=$(clicked).parent().parent().parent().siblings('.hotdeal').children('.productDescription').children('.productName').children("h5")

    let oldprice=$(clicked).parent().parent().parent().siblings('.hotdeal')
        .children('.productDescription').children('.productPrice').children('.through').children()

    let newprice=$(clicked).parent().parent().parent().siblings('.hotdeal')
        .children('.productDescription').children('.productPrice').children('.realPrice').children()

    let anchor=$(clicked).parent().parent().parent().siblings('.hotdeal')
        .children('.productDescription').children('.rate').children('a')[0]

    let image=$(clicked).parent().parent().parent().siblings('.hotdeal')
        .children('.productImg').children('img')

    
       
        nameProductofTargeted.text(name)
        oldprice.text(oldPrice + "$")
        newprice.text(newPrice + "$") 
        image.attr('src',imagesrc)
        anchor.href= `deals/${link}`

}



function adapi(){
    url='/adapi/'
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        }})
        .then(response=>{ return response.json()})
        .then(data=>{

            var ij=0;
            var ik=0;
            //get slider container
            let slidercont=document.getElementById("imageslidecontainer");
            
            let sliderparent=document.querySelector(".rightsidecont .slider")
          
            
        setInterval(() => {

            if(ik <= data["sliders"].length - 1){
                var newsrcimg=data["sliders"][ik].image
                var newsrcvideo=data["sliders"][ik].video
                var newbtntext=data["sliders"][ik].button
                var newurlbutton=data["sliders"][ik].urlbutton
                let btnslider=document.getElementById("btnslider");

                if(newsrcimg && !newbtntext){
                    if(btnslider){
                        btnslider.remove()
                    }

                    slidercont.children[0].setAttribute('src',newsrcimg);
                    

                }else if(newsrcimg && newbtntext && newurlbutton){
                    
                    var textbtnnode=document.createTextNode(newbtntext)
                    slidercont.children[0].setAttribute('src',newsrcimg);


                    var createddiv=document.createElement("div")
                    var createda=document.createElement("a")
                    var createdbtn=document.createElement("button")
                    

                   
                    createddiv.setAttribute('id','btnslider')
                    createddiv.classList.add('shopNow')
        
                    createdbtn.appendChild(textbtnnode)
                    createda.setAttribute('href',newurlbutton)
                    createda.appendChild(createdbtn)

                    createddiv.appendChild(createda)

                    if(btnslider){
                        btnslider.remove()
                    
                    
                    }
                    sliderparent.appendChild(createddiv)
                    
                }
         
                ik++

            }else{

                ik=0

            }

        }, 2000);
            
            
            
            
            
            
            
            //get  the vertical add container
        let addvertical=document.getElementById('adImage');
        
        if(data['verticalAd'][ij]){
        setInterval(() => {
            let url = data['verticalAd'][ij];
            addvertical.childNodes[1].setAttribute('src',url)

            if(ij < data['verticalAd'].length - 1){
                ij++;
            }else{
                ij=0
            }
        }, 2000);
    }
        })  
}
// //update the products on click the catigory ysing api


function hotdealupdate(clicked){
    url='/hotdeals/'
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        }}).then(response=>{ return response.json()}).then(data=>{
           
            var targetedsectionD= clicked.dataset.section
            
            hotdealdata = data;
            
         let productname=hotdealdata[targetedsectionD][hotdealKey]['name']
         let priceOld =hotdealdata[targetedsectionD][hotdealKey]['old_price']
         let pricenew = hotdealdata[targetedsectionD][hotdealKey]['new_price']
         let srcImage = hotdealdata[targetedsectionD][hotdealKey]['image']
         let rate = hotdealdata[targetedsectionD][hotdealKey]['rate']
    //    if(i <0 || i>hotdealdata[targetedsectionD].length){
    //        i=0
    //    }else{

    //    }

       if(clicked.dataset.direct == 'left'){
            if(hotdealKey <=0 ){
                hotdealKey=hotdealdata[targetedsectionD].length
            }
            hotdealKey-=1 
            
            contentHotdeals(clicked,productname, priceOld,pricenew,srcImage,productname)
            
        }else{
            hotdealKey+=1
            if( hotdealKey > hotdealdata[targetedsectionD].length - 1){
                hotdealKey=0
            }
            
            contentHotdeals(clicked,productname, priceOld,pricenew,srcImage,productname)
            
            
        }
           
        })
}
// //function of making an api and use it though
function updateproducts(category,categoryId,section){
    url="/updateproducts/"
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "category":category,
            "id":categoryId
            
            
        })
    })
    .then((response)=>{
        return response.json()
    })
     .then((data)=>{
        

        //get the data object transfered and get the specific clicked category 
        
        
        //access the category array associated

        
        // goto the products container and change the innerhtml
        var productsCont=document.querySelectorAll("#productsCont")
        
        //empty the container
       
        productsCont[section].innerHTML=''
        if(categoryId && categoryId > 0){
            var ctgProducts = data["categorizedProducts"][categoryId - 1][category]

            for(var i=0;i<ctgProducts.length;i++){
                var val=0
                var newpricepromo= ctgProducts[i].new_price
                var oldpricepromo= ctgProducts[i].old_price
                var promotion=(parseInt(newpricepromo) / parseInt(oldpricepromo))*100
                if(promotion.toString().split('').length >= 2){
                    val= promotion.toString().split('').slice(0,2).join('')
                               }

                
                           
                productsCont[section].innerHTML +=`
               
                <div class="product">
                <a href='product/${ctgProducts[i].id}'>
                ${
                    ctgProducts[i].is_promotion?
                       `<div id="promo${ctgProducts[i].id}sp" class="promotion">`
                           +  val +'%' +
                       `</div>`
                    
                :
                ''
            }
                    <div class="productImg">
                        <img class="skeleton" src=" ${ctgProducts[i].image}" alt="">
                    </div>
                </a>
                    
                    <div class="productDescription">
                        <div class="productName skeleton-text">
                            <h5>${ ctgProducts[i].name }</h5>
                        </div>
                        <div class="productPrice">
                            <div class="through skeleton-text">
                                ${ ctgProducts[i].old_price <=0 ? 
                                `<p>Free</p>`
                                : 
                                `<p>${ctgProducts[i].old_price}$</p>`
                                }
                                    
                                
                            </div>
                            <div  class="realPrice skeleton-text">
                                <h5>${ ctgProducts[i].new_price <= 0? 
                                    `Free`
                                    : 
                                    `${ctgProducts[i].new_price}$`
                                    }</h5>
                            </div>
                        </div>
                        <div class="rate">
                        ${ctgProducts[i].rate == 0?
                        `<i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 0.5?

                        `<i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 1?
                            
                        `<i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 1.5?
                        
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 2?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 2.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 3?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 3.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 4?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 4.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        ctgProducts[i].rate == 5.5?
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
                            <button data-product='${ctgProducts[i].id}' data-action='add'  class="addToCart">Add to cart</button>
                            
                        </div>
                        </div>
                        
                </div>
            `

            }
        }else{
            
            var allProducts = data["allProducts"];

            for(var i=0;i<allProducts.length;i++){
                var val=0
                var newpricepromo= allProducts[i].new_price
                var oldpricepromo= allProducts[i].old_price
                var promotion=(parseInt(newpricepromo) / parseInt(oldpricepromo))*100
                if(promotion.toString().split('').length >= 2){
                    val= promotion.toString().split('').slice(0,2).join('')
                               }


                productsCont[section].innerHTML +=`
               
                <div class="product">
                <a href='product/${allProducts[i].id}'>
                ${
                    allProducts[i].is_promotion?
                       `<div id="promo${allProducts[i].id}sp" class="promotion">`
                           +  val +'%' +
                       `</div>`
                    
                :
                ''
            }
                    <div class="productImg">
                        <img class="skeleton" src=" ${allProducts[i].image}" alt="">
                    </div>
                </a>
                    
                    <div class="productDescription">
                        <div class="productName skeleton-text">
                            <h5>${ allProducts[i].name }</h5>
                        </div>
                        <div class="productPrice">
                            <div class="through skeleton-text">
                                ${ allProducts[i].old_price <=0 ? 
                                `<p>Free</p>`
                                : 
                                `<p>${allProducts[i].old_price}$</p>`
                                }
                                    
                                
                            </div>
                            <div  class="realPrice skeleton-text">
                                <h5>${ allProducts[i].new_price <= 0? 
                                    `Free`
                                    : 
                                    `${allProducts[i].new_price}$`
                                    }</h5>
                            </div>
                        </div>
                        <div class="rate">
                        ${allProducts[i].rate == 0?
                        `<i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 0.5?

                        `<i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 1?
                            
                        `<i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 1.5?
                        
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 2?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 2.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 3?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 3.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 4?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 4.5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 5?
                        `<i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star"></i>`
                        :
                        allProducts[i].rate == 5.5?
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
                            <button data-product='${allProducts[i].id}' data-action='add'  class=" addToCart">Add to cart</button>
                            
                        </div>
                        </div>
                        
                </div>
            `
        }
            
        
       
   }})
}


//on click on left and right arrows

var arrowscntprod= document.querySelectorAll('.arrows .arrowscont i');
var arrowsdeals= document.querySelectorAll('.arrows .dealarrow i');

for(var i=0; i<arrowscntprod.length;i++){
   
    arrowscntprod[i].addEventListener('click',function(e){
     
        var productscontainerElement = $(this).parent().parent().parent().parent().parent().siblings(".products")
        var selectedNow= $(this).parent().parent().siblings(".selectedCategory");
        var lastoftype= $(this).parent().parent().siblings(".category:last-of-type");
        var firstoftype= $(this).parent().parent().siblings(".category:first-of-type");
        var width=productscontainerElement.width()
        let aa= $(this).parent().parent().parent().parent().parent().siblings(".products")
        let lengthoflists= selectedNow.siblings().length
       
        //this commented lines are for changing the targeted category on click on chevron
    //    if(this.dataset.direct == "right" && selectedNow.data('category') <  lengthoflists + 1 ){

    //     selectedNow.next().addClass('selectedCategory').siblings().removeClass('selectedCategory');
    //     selectedNow.next().click()
       
    //    }

    //    else if(this.dataset.direct == "right" && selectedNow.data('category') ==  lengthoflists + 1){
        
    //     lastoftype.css('color','red');
    //    }

    //    if(this.dataset.direct == "left" && selectedNow.data('category') >  0 ){
        
      
    //      selectedNow.prev().addClass('selectedCategory').siblings().removeClass('selectedCategory');
    //      selectedNow.prev().click()
            
    //     }
        
    //     else if(this.dataset.direct == "left" && selectedNow.data('category') == 0 ){
            
    //         firstoftype.css('color','red');
    //     }


        this.dataset.direct == 'right'?
            productscontainerElement.animate({
            scrollLeft :  `+=${width + 2}` + 'px'
            },800)
        :
            productscontainerElement.animate({
                scrollLeft :  `-=${width + 2}` + 'px'
                },800)

        
    })
}




// //when click o btn to scroll
// $(window).ready(function(){
    
   
    
//trying to make the products container dragable


var productsEle= document.getElementsByClassName("products");
var mouseDownOnProductsCont=false;
var scrollleft;
var xaxis;
var positionwalked;

for(var i=0;i<productsEle.length;i++){
    productsEle[i].addEventListener('mousedown',function(e){
        e.preventDefault();
        e.stopPropagation()
        mouseDownOnProductsCont=true;

        xaxis=e.pageX - this.offsetLeft;
        scrollleft= this.scrollLeft;
    });

    

    productsEle[i].addEventListener('mousemove',function(e){
       
        if(mouseDownOnProductsCont){
            e.preventDefault();
            this.classList.add("scaledrag")
           
            this.style.cursor = 'grabbing'
            var currentXaxis= e.pageX - this.offsetLeft;
            positionwalked = currentXaxis - xaxis;
            this.scrollLeft = scrollleft - positionwalked
       }else{
        e.stopPropagation()
        e.preventDefault();
       }

    })

    productsEle[i].addEventListener('mouseup',function(e){
        e.preventDefault();
        e.stopPropagation();
        this.classList.remove("scaledrag")
        mouseDownOnProductsCont=false;
        this.style.cursor = 'grab'
    })
    productsEle[i].addEventListener('mouseleave',function(e){
        this.classList.remove("scaledrag")
        mouseDownOnProductsCont=false;
        this.style.cursor = 'grab'
    })

}


//on click on arrows of the deals content

for(var i=0;i<arrowsdeals.length; i++){
    arrowsdeals[i].addEventListener('click',function(){
        
        hotdealupdate(this)
    })
}

window.onload = function(){
    adapi()
}



window.addEventListener("scroll",function(e){
    var horad=document.getElementById('horAd');
    let firstP=$('.shopnowdesc p:first-of-type')
    let secondP=$('.shopnowdesc p:last-of-type')
    let btnhorad=$('.shopnowdesc a')
    let imgAd=$('.shopnowImg img')
    let imgaddsrc=document.querySelector('.shopnowImg img').getAttribute("src")
   
    
  

    


    if(horad.offsetTop  < ($(window).scrollTop() +  2.4*horad.clientHeight)){
        if(imgaddsrc.includes('.gif') || imgaddsrc.includes('.png') ){
            imgAd.fadeIn(300)
        }
        
        firstP.show(800)
        secondP.show(500)
        btnhorad.fadeIn(100)
        
    }else{
        firstP.hide(500)
        secondP.hide(500)
        btnhorad.fadeOut(500)

        if(imgaddsrc.includes('.gif') || imgaddsrc.includes('.png') ){
            imgAd.fadeOut(800)
        }
        
    }

    
        

    
   
})



