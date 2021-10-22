from .models import *

def callwishnumber(request):
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.all().filter(customer=request.user)
    else:
        wishlist=[]
    return len(wishlist)

def callcartnumber(request):
    items= OrderItem.objects.all()
    itemsordered=[]
    category=CategoryList.objects.all()
    if request.user.is_authenticated:
        
        totalItem=0
        totalarray=[]
        for item in items:
            if item.order.customer:
                if request.user == item.order.customer and item.order.complete == False:
                    
                    itemsordered.append(item)
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
       

        totalPrice=sum([int(item.product.new_price) * int(item.quantity) for item in itemsordered])
        
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}
    return {"total":total, "products":itemsordered}


def existwishproduct(request):
    try:
        wishlists=Wishlist.objects.all().filter(customer=request.user)
    except :
        wishlists=[]
    exist=False
    if wishlists:
        for product in wishlists:
            if product.product == Product.objects.get(id=1):
                exist= True
            else:
                exist=exist
        
    return exist