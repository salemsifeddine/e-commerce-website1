
let inputSearchField= document.getElementById("search")
let dropDown = document.getElementById("dropdownmenusearch")
let searchBtn= document.getElementById("searchinput-btn")

function getSearchList(querySearchArray){
    url="/apilistSearch/"


    

    fetch(url,{
        method:"GET",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        }
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        //
        var realDataList=[]
        for(var q=0; q<querySearchArray.length;q++){

            for(var v=0; v<data.list.length;v++){
                if(data.list[v].includes(querySearchArray[q])){
                    realDataList.push(data.list[v])
                }
            }
            
        }

        
        dropDown.innerHTML=''
        for(var li=0; li< realDataList.slice(0,6).length;li++){
           
            var liEle=document.createElement("li")
            var liContent= document.createTextNode(realDataList[li])
            liEle.appendChild(liContent)
            dropDown.appendChild(liEle)
        }
        
        var dropDownList = document.querySelectorAll("#dropdownmenusearch li")

        if(dropDown.style.display == "block"){
            for(var l=0; l < dropDownList.length; l++){
                
                dropDownList[l].addEventListener("click",function(){
                   var clickedList = this.textContent
                   inputSearchField.value =this.textContent
                   searchBtn.click()
                        // window.location.href="search/?q=" + this.textContent
                })
            }
        }

        //
    })
}

inputSearchField.addEventListener('keyup',function(e){
    
    e.preventDefault();
    searchValue= e.target.value.split(" ");
    realSearch=[]
    dropDown.style.display="block"




    for(var k=0; k< searchValue.length;k++){
        var searchLower= searchValue[k].trim().toLowerCase()
        if(searchValue[k]){
            realSearch.push(searchLower)
           
        }
    }
    
    getSearchList(realSearch)

    
})


//
if(document.getElementById("btnloadsearch")){
    var loadsearchbtn = document.getElementById("btnloadsearch");

    loadsearchbtn.addEventListener("click",function(){
        this.dataset.rows=parseInt(this.dataset.rows)+1
        var slicenum = this.dataset.rows
        var query= this.dataset.query
        var loads=this.dataset.load
        
        loadSearch(query,slicenum,this,loads)
    })
}


//function of making an api and use it though
function loadSearch(cat,sliceno, clickedbtn,loads){
    url="/rows/"
    
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "load":loads,
            "query":cat,
            "rows":sliceno,
           
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((product)=>{
        
        if(product.all == "yes"){
            clickedbtn.remove()
        }

        document.getElementById("productSearchCont").innerHTML=''
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

            
                       
            document.getElementById("productSearchCont").innerHTML +=`
           
            <div class="product-search">
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
        var buttons = document.getElementsByClassName("addToCart")
        for(var i=0; i<buttons.length; i++){
            buttons[i].addEventListener("click",function(){
                
                id=this.dataset.product
                action=this.dataset.action
              
                if(user == "AnonymousUser"){
                    // getCookieItem(id,action)
                    
                    console.log("ss")
                    
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
        
        }

       

        //
    })
}


