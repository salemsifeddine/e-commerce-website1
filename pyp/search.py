from django.db.models import Q
from .models import *
from .forms import *

strip_words= ["an","a","on","in","from","for",'by',"not",'of','then',"to","with","the","that"]


def store(request, query):
    if query > 2:
        search=SearchItem()
        search.query=query
        search.ip_addres=request.META.get("REMOTE-ADDR")
        search.user=None
        if request.user.is_authenticated():
            search.user = request.user
          
        search.save() 

def getprodFiltered(search_text):
    words=prepare_txt(search_text)
    products=Product.objects.all()
    result={}
    result["products"]=[]
    productsfiltered=[]

    for word in words:
        productsfiltered += products.filter(Q(name__icontains =word) | Q(description__icontains=word) | Q(sku__iexact=word) | Q(description__icontains=word) | Q(brand_name__icontains=word) | Q(meta_description__icontains=word) | Q(meta_keywords__icontains=word) )
    
    seted=set(productsfiltered)
   
    result['products']=seted

    return result


def prepare_txt(search_text):
    words=search_text.split()
    
    for common in strip_words:
        if common in words:
            words.remove(common)
    return words[0:5]


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def suggestedProduct(request):
    sugestedforUser=SearchItem.objects.all().filter(user=request.user)
    products=Product.objects.all()
    searchUser=[]
    result={}
    result["suggested"]=[]
    productsfiltered=[]

    for sgstd in sugestedforUser:
        searchUser.append(sgstd)
    
   
    

    for word in searchUser:
        productsfiltered += products.filter(Q(name__icontains =word) | Q(description__icontains=word) | Q(sku__iexact=word) | Q(description__icontains=word) | Q(brand_name__icontains=word) | Q(meta_description__icontains=word) | Q(meta_keywords__icontains=word) )
    
    seted=set(productsfiltered)

  
    result['suggested']=seted

    
    return result