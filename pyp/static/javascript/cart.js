

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



//********** */
//change profile picture when user get uploaded his photo and before submit it




