

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




