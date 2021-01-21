from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.views import generic
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import xlsxwriter
from random import randrange
# Create your views here.


def base(response):
    
    context={"name":"E-COMMERCE"}
    return render(response,"pages/base.html",context)


def main(response):
    products=Product.objects.all()
    options= Catigory.objects.all()
    if response.user.is_authenticated:
        items= OrderItem.objects.all()
        totalItem=0
        totalarray=[]
        for item in items:
            if item.order.customer:
                 if response.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
                
        totalPrice=sum([item.product.new_price * item.quantity for item in items])
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}
    context={"name":"E-COMMERCE","title":"acceil","products":products,"options":options,"totalitem":total}
    return render(response,"pages/main.html", context)


def cart(response):
    #order= Order.objects.all()
    items= OrderItem.objects.all()
    
    if response.user.is_authenticated:
        
        totalItem=0
        totalarray=[]
        for item in items:
            if item.order.customer:
                if response.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)

        totalPrice=sum([item.product.new_price * item.quantity for item in items])
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}

    context={"name":"E-COMMERCE", "title":"cart", "items":items,"totalitem":total}
    return render(response, "pages/cart.html", context)



def checkout(response):
    items=OrderItem.objects.all()
    totalItem=0
    totalarray=[]
    if response.method != 'POST':
        form=CustomInfo()
    else:
        form = CustomInfo(data= response.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    if response.user.is_authenticated:
        for item in items:
            if item.order.customer:
                if response.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
                    
        #totalPrice=sum([item.product.new_price * item.quantity for item in ttl])
        total={"item":totalItem}
    else:
        total={"item":0}

    context={"name":"E-commerce", "title":"checkout", "items":items,'form':form,"totalitem":total}
    return render(response, "pages/checkout.html", context)


def login(response):
    return render(response, 'pages/login.html')


def signin(response):
    if response.method != 'POST':
            form=CustomInfo()
            
    else:
        form = CustomInfo(data= response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={"name":"E-COMMERCE","title":"SIGN IN", "form":form}
    return render(response, "pages/signin.html",context)


def logout(response):
    auth.logout(response)
    return redirect("/login")


@login_required
def profil(request):
    
    if request.method == 'POST':
        form = Photoprofile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() :
            form.save()
            return redirect("/profil")
    else:
        form = Photoprofile(instance=request.user.profile)

    if request.user.is_authenticated:
        items= OrderItem.objects.all()
        totalItem=0
        totalarray=[]
        for item in items:
            if item.order.customer:
                if request.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
                
        totalPrice=sum([item.product.new_price * item.quantity for item in items])
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}
    context={"name":"Profile",'title':"E-COMMERCE","form":form,"totalitem":total}
    return render(request, "pages/profile.html",context)



class ProductDetailView(generic.DetailView):
    model=Product
    template_name="pages/detail.html"



#add product view
@login_required
def addproduct(response):
    if response.method == 'POST':
        form = ImagePro(response.POST, response.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.owner=response.user
            form.save()
            return redirect("home")
    else:
        form = ImagePro()

    if response.user.is_authenticated:
        items= OrderItem.objects.all()
        totalItem=0
        totalarray=[]
        for item in items:
            if response.user == item.order.customer:
                quantm= item.quantity
                totalarray.append(quantm)
                totalItem = sum(totalarray)
                
        totalPrice=sum([item.product.new_price * item.quantity for item in items])
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}
    context={"name":"E-commerce", "title":"New Product","form":form,"totalitem":total}
    return render(response, "pages/AddProduct.html",context)

##my products 
@login_required
def myproducts(request):
    data=Product.objects.all()
    if request.user.is_authenticated:
        items= OrderItem.objects.all()
        totalItem=0
        totalarray=[]
        for item in items:
            if item.order.customer:
                if request.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
                
        totalPrice=sum([item.product.new_price * item.quantity for item in items])
        total={"price":totalPrice, "item":totalItem}
    else:
        total={"price":0, "item":0}
    context={"name":"E-commerce", "title":"My Products","data":data,"totalprice":total,"totalitem":total}
    
    return render(request, "pages/myproducts.html", context)

#JsonResponse

def UpdateItem(request):
    data= json.loads(request.body.decode('utf-8'))
    idproduct=data['productId']
    action=data["action"]
    product= Product.objects.get(id=idproduct)
    order, created= Order.objects.get_or_create(customer=request.user, complete=False)
    orderItem, created= OrderItem.objects.get_or_create(order=order, product=product)
    
        
    if action == "add":
       orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    totalItem=sum([item.quantity for item in OrderItem.objects.all()])
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        #order.delete()
   
    
    

    data_json = {
        'name':orderItem.product.name,
        'price':orderItem.product.new_price,
        'totalCart':totalItem
    }

    return JsonResponse(data_json, safe=False)

@csrf_exempt
def ShippingApi(request):
    data= json.loads(request.body)

    items=OrderItem.objects.all()
    ship=ShippingAddress.objects.all()
    
    producthasbeenordered=[]
    
    for item in items:
        if request.user.is_authenticated:
            if item.order.customer == request.user:
                itemname=item.product.name
                itemprice=item.product.new_price
                itemquantity=item.quantity
                proditem = {
                    "product":itemname,
                    "price":itemprice,
                    "quantity":itemquantity
                }
                producthasbeenordered.append(proditem)



    address=data["address"],
    state=data["state"],
    city=data["city"],
    zipcode=data["zip"],
    customer=request.user
    #ordered=data["ordered"]

    datapassed={
        "address":data["address"],
        "state":data["state"],
        "city":data["city"],
        "zip":data["zip"],
        "customer":request.user.username,
        "customer email":request.user.email,
        "ordered":producthasbeenordered
    }

    ##start our work excel

    work = xlsxwriter.Workbook("data1.xlsx")
    sheet=work.add_worksheet()

    for idk, shi in enumerate(ship):
    #    print(shi.state[0], idk)
        sheet.write(f"A{idk}",shi.customer.username)
        sheet.write(f"B{idk}",str(shi.order))
        sheet.write(f"C{idk}",shi.address)
        sheet.write(f"D{idk}",shi.city)
        sheet.write(f"E{idk}",shi.state)
        sheet.write(f"F{idk}",str(shi.zip_code))

    work.close()

    #end excel work

    order, created= Order.objects.get_or_create(customer=customer, complete=False)
    ship, created = ShippingAddress.objects.get_or_create(customer=customer,order=order,address=address,city=city,state=state,zip_code=zipcode)
    ship.save()
    return JsonResponse(datapassed, safe=False)
