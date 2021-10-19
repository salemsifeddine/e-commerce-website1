if(document.getElementsByClassName('removewish')){
    var removewish = document.getElementsByClassName('removewish')

    for(var wishbtndelete= 0;wishbtndelete< removewish.length;wishbtndelete++){
        removewish[wishbtndelete].addEventListener('click', function(){
            var idWish= this.dataset.id
            console.log(idWish)
            wishlistApi(idWish,'removewish')
        })
    }
}else{
    setTimeout(() => {
        var removewish = document.getElementsByClassName('removewish')

        for(var wishbtndelete= 0;wishbtndelete< removewish.length;wishbtndelete++){
            removewish[wishbtndelete].addEventListener('click', function(){
                var idWish= this.dataset.id
                console.log(idWish)
                wishlistApi(idWish,'removewish')
            })
        }
    }, 5000);
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