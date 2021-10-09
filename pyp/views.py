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
from .serializers import APISerializer, APISerializerCat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .search import *

# Create your views here.


clickedCategoryid=""

class Apiclass(APIView):
    def get(self,request):
        category=CategoryList.objects.all()
        allproducts=Product.objects.all()
        serializer=APISerializer(allproducts, many=True)
        
    
        data_json={
            'products':"productsarray"
        }
        return Response(serializer.data)

    def post(self):
        pass


def base(response):
    # form=SearchForm()

    # if response.method == 'POST':
    #     form=SearchForm(data=response.POST)
    #     if form.is_valid():
            
    
    products=Product.objects.all()

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
    
   
    context={"name":"E-COMMERCE","totalitem":total,"form":"form"}
    return render(response,"pages/base.html",context)

def adsapi(request):

    imagesverAd=AdBanner.objects.all()
    

    imagesverAdarray=[]
    sliderarray=[]
    for image in imagesverAd:
        imagesverAdarray.append(image.image.url)

    for slide in Slider.objects.all():
        if slide.video and slide.button and not slide.image :
            sliderarray.append({'image':'',"video":slide.video.url, "button":slide.button,"urlbutton":slide.urlbutton })
        elif slide.video and not slide.button and not slide.image:
            sliderarray.append({'image':'',"video":slide.video.url, "button":'',"urlbutton":'' })
        elif slide.video and  slide.button and not slide.urlbutton and not slide.image:
            sliderarray.append({'image':'',"video":slide.video.url, "button":'',"urlbutton":'' })
        elif slide.image and slide.button and not slide.video:
            sliderarray.append({'image':slide.image.url,"video":"", "button":slide.button,"urlbutton":slide.urlbutton })
        elif slide.image and not slide.button  and not slide.video:
            sliderarray.append({'image':slide.image.url,"video":"", "button":"","urlbutton":"" })
        elif slide.image and slide.button and not slide.urlbutton  and not slide.video:
            sliderarray.append({'image':slide.image.url,"video":"", "button":"","urlbutton":"" })
        else:
            pass

    object_json={"verticalAd":imagesverAdarray,
                "sliders":sliderarray}

    
    return JsonResponse(object_json,safe=False)


def main(request):
    
    category=CategoryList.objects.all()
    allproducts=Product.objects.all()
    
    products={"featured":allproducts.filter(is_featured=True),
                "bestseller":allproducts.filter(is_bestseller=True),
                "products":allproducts.order_by("-date_added")}
    form=''
   
        
    options= CategoryList.objects.all()
    category=CategoryList.objects.all()
    exist=False;

    if request.method != 'POST':
        form=EmailField()
    else:
        form = EmailField(data=request.POST)
        enteredEmail=form.data['email'];

        for email in NewsLetterEmails.objects.all():
            if enteredEmail == email.email:
                print(email.email)
                exist=True
            
        if form.is_valid() and  not exist:
            form.save()
            return redirect('home')
       


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
    context={"name":"E-COMMERCE","title":"acceil","products":products,"options":options,"totalitem":total,
    "category":category,"form":form}
    return render(request,"pages/main.html", context)


def cart(response):
    #order= Order.objects.all()
    items= OrderItem.objects.all()
    category=CategoryList.objects.all()
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
    category=CategoryList.objects.all()
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
    category=CategoryList.objects.all()
    return render(response, 'pages/login.html')


def signin(response):
    category=CategoryList.objects.all()
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
    category=CategoryList.objects.all()
    auth.logout(response)
    return redirect("/login")


@login_required
def profil(request):
    category=CategoryList.objects.all()
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
    def get_context_data(self,**kwargs):
        total = super().get_context_data(**kwargs)
        products = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            items= OrderItem.objects.all()
            totalItem=0
            totalarray=[]
            for item in items:
                if  self.request.user == item.order.customer:
                    quantm= item.quantity
                    totalarray.append(quantm)
                    totalItem = sum(totalarray)
                    
            totalPrice=sum([item.product.new_price * item.quantity for item in items])
            total["totalitem"]={"price":totalPrice, "item":totalItem}
        else:
            total["totalitem"]={"price":0, "item":0}

        total["products"]=Product.objects.all()
        
        return total


#add product view
@login_required
def addproduct(response):
    category=CategoryList.objects.all()
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
    category=CategoryList.objects.all()
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
    category=CategoryList.objects.all()
    data= json.loads(request.body.decode('utf-8'))
    idproduct=data['productId']
    action=data["action"]
    if data["quantity"]:
        quantity=data["quantity"]
    else:
        quantity=1
    product= Product.objects.get(id=idproduct)
    order, created= Order.objects.get_or_create(customer=request.user, complete=False)
    orderItem, created= OrderItem.objects.get_or_create(order=order, product=product)
    

    if action == "add" and quantity:
       orderItem.quantity = (orderItem.quantity + quantity)
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
        'totalCart':totalItem,
        
    }

    return JsonResponse(data_json, safe=False)



def UpdateProducts(request):
    data= json.loads(request.body.decode('utf-8'))
    clickedCategory=data['category']
    allproducts=Product.objects.all()
    category=CategoryList.objects.all()

    selectedProducts=allproducts.filter(catigory=data['id'])
    clickedCategoryid=data['id']
    
   
    serializer=APISerializer(allproducts, many=True)
    serializercat=APISerializerCat(category, many=True)
    AllProductsArray=[]
    AllCategorizedProducts=[]
    objectdata=[]
    for product in allproducts:
        data_json={
            'id':product.id,
            'name':product.name,
            'image':product.image.url,
            'description':product.description,
            'category':product.catigory.categoryName,
            'old_price':product.old_price,
            'new_price':product.new_price,
            'owner':product.owner.username,
            'rate':product.rate.rate,
        }
        AllProductsArray.append(data_json)

    
       
    if clickedCategoryid and clickedCategoryid:


        for ctg in category:
                newobj={}
                productsarranged=[]
                for product in AllProductsArray:
                    
                    if product['category'] == ctg.categoryName:
                        productsarranged.append(product)
                    
                    newobj={ctg.categoryName:productsarranged}
                objectdata.append(newobj)   
    
    

 

    

    data_object={
        'allProducts':AllProductsArray,
        'categorizedProducts':objectdata,
        

    }
            
   

    return JsonResponse(data_object, safe=False)


def HotdealsApi(request):
    hotdeals=Hotdeals.objects.all()
    object_data1={}
    hotdealsarray=[]
    for hotdeal in hotdeals:
        
        hotdealsobj={
            'id':hotdeal.id,
            'originalproductid':hotdeal.product.id,
            'name':hotdeal.product.name,
            'image':hotdeal.product.image.url,
            'description':hotdeal.product.description,
            'category':hotdeal.product.catigory.categoryName,
            'old_price':hotdeal.product.old_price,
            'new_price':hotdeal.product.new_price,
            'owner':hotdeal.product.owner.username,
            'rate':hotdeal.product.rate.rate,
        }
        hotdealsarray.append(hotdealsobj)
        object_data1={
            'data':hotdealsarray
        }
    return JsonResponse(object_data1, safe=False)


@csrf_exempt
def ShippingApi(request):
    category=CategoryList.objects.all()
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


def category(request,category):
    category=CategoryList.objects.all()

    return render(request, "pages/category.html",context={})

def search(request):
    searchData=SearchItem.objects.all() 
    try:
        q=request.GET.get("q")
    except:
        q=None
    
    if q:
        pagename="pages/search.html"
        query=q
    else:
        pagename="pages/search.html"

    ip=get_client_ip(request)
    result= getprodFiltered(q)
    if request.user.is_authenticated:
        
        searchData, created = searchData.get_or_create(query=q, ip_addres=ip, user=request.user)
        searchData.save()
    else:
        searchData, created = searchData.get_or_create(query=q, ip_addres=ip, user=None)
        searchData.save()
         
    return render(request,"pages/search.html",context={"query":query,"products":result["products"]})



def listSearch(request):
        
    allproducts=Product.objects.all()
    productNames=[]
        
    for product in allproducts:
        productNames.append(product.name)
        
    data_json ={
        "list" :productNames
    }

    return JsonResponse(data_json,safe=False)

