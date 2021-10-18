if(document.getElementById('removewish')){
    var removewish = document.getElementById('removewish')

    removewish.addEventListener('click', function(){
        var idWish= this.dataset.id
        wishlistApi(idWish,'remove')
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