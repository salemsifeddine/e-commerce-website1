
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


