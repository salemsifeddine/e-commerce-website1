var buttons = document.getElementsByClassName("addToCart")
for(var i=0; i<buttons.length; i++){
    buttons[i].addEventListener("click",function(){
        
        id=this.dataset.product
        action=this.dataset.action
      
        if(user == "AnonymousUser"){
            console.log("not logged In")
        }
        else{
            console.log("here")
           //cal your api and five it the keys
           update(id,action)
        
            
        }
    })
}


//function of making an api and use it though
function update(id,action){
    url="/update/"
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body: JSON.stringify({
            "productId":id,
            "action":action
            
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


//function when clicking on Continue btn shipping form
btn=document.getElementsByClassName('ship')

function shipping(){
    //get inputs
    address= document.getElementById("address").value
    city= document.getElementById("city").value
    state= document.getElementById("state").value
    zip= document.getElementById("zip").value
    //console.log(address, city, state, zip)

    //get ordered products and parse them
    orderedName=document.getElementsByClassName("orderedname")
    orderedPrice=document.getElementsByClassName("orderedprice")
    orderedQuantity=document.getElementsByClassName("orderedquantity")
    

    //ORDERPRO=[]
    //for(var i=0; i< orderedName.length; i++){
    //    orderuser ={
    //        "name":orderedName[i].textContent,
    //        "price":orderedPrice[i].textContent,
    //        "quantity":orderedQuantity[i].textContent
    //    }
    //    ORDERPRO.push(orderuser)
    //}


    url = "/shipping/"
    fetch(url,{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-CSRFToken":csrftoken
        },
        body:JSON.stringify({
            "address":address,
            "state":state,
            "city":city,
            "zip":zip,
        })
        })
        .then((response)=>{
            return response.json()
        })
        .then((data)=>{
            console.log(data)
            

        })
}

for(var i=0; i<btn.length; i++){
    btn[i].addEventListener('click',function(e){
        e.preventDefault()
        shipping()
        this.submit()
    })
}

//********** */
//change profile picture when user get uploaded his photo and before submit it

