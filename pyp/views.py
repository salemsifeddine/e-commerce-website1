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
from django.db.models import Q
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.views import  View
from django.core.mail import send_mail, EmailMessage
import pdfkit
import datetime
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


def base(request):
    # form=SearchForm()

    # if response.method == 'POST':
    #     form=SearchForm(data=response.POST)
    #     if form.is_valid():
            
    
    products=Product.objects.all()
    wishlists=Wishlist.objects.all()

    
    
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)
    context={"name":"E-COMMERCE","totalitem":total,"form":"form","wishlist":wishlist,
    "wishlists":wishlists}
    return render(request,"pages/base.html",context)

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

from .cartandwish import *

def main(request):
    totalwish=callwishnumber(request)
    
    
    category=CategoryList.objects.all()
    allproducts=Product.objects.all()
    suggestedProducts=''
    if request.user.is_authenticated:
        
        suggestedProducts=suggestedProduct(request)
        suggestedProducts=suggestedProducts["suggested"]
        
    else:
        suggestedProducts= allproducts.filter(is_featured=True)
 
    
    
    products={"featured":allproducts.filter(is_featured=True),
                "bestseller":allproducts.filter(is_bestseller=True),
                "products":allproducts.order_by("-date_added"),
                "suggested":suggestedProducts,
                "hotdeal":Hotdeals.objects.all().last(),
                "specialdeal":SpecialDeal.objects.all().last()
               }
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
               
                exist=True
            
        if form.is_valid() and  not exist:
            form.save()
            return redirect('home')
       
    hotdeals=Hotdeals.objects.all()
    specialdeals=SpecialDeal.objects.all()

    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)
    context={"name":"E-COMMERCE","title":"acceil","products":products,"options":options,
    "hotdeals":hotdeals,"specialdeals":specialdeals,
    "wishlist":wishlist,"totalitem":total,
    "category":category,"form":form}
    return render(request,"pages/main.html", context)


def cart(response):
    #order= Order.objects.all()
   
    total=callcartnumber(response)['total']
    wishlist=callwishnumber(response)
    itemsordered= callcartnumber(response)['products']
    context={"name":"E-COMMERCE", "title":"cart", "items":itemsordered,"totalitem":total,"wishlist":wishlist}
    return render(response, "pages/cart.html", context)


shipDATA={}
def checkout(request):
    category=CategoryList.objects.all()
    itemsordered=[]
    items=OrderItem.objects.all()
   
    totalItem=0
    totalarray=[]
    totalPrice=[]
    if request.method != "POST":
        form = ShippingForm()
     
    else:
        # order, created= Order.objects.get_or_create(customer=customer, complete=False)


        form= ShippingForm(request.POST)
        if form.is_valid():
            order= Order.objects.filter(customer=request.user,complete=False ).first()
            # order.complete= True
            order.complete = True 
            order.save()
            # trans=Order.objects.get(customer=response.user, complete=False).first().complete = True
            # trans.save()

            post=form.save(commit=False)
            post.customer=request.user
            post.order=Order.objects.all().filter(customer=request.user, complete=False).first()
            
            shipDATA["name"]= post.customer
            shipDATA["address"]= post.address
            shipDATA["zip_code1"]= post.zip_code1
            shipDATA["zip_code2"]= post.zip_code2

            
            

            post.save()
            return redirect("home")
            
    
        
    total=callcartnumber(request)['total']
    
    wishlist=callwishnumber(request)
    itemsordered= callcartnumber(request)['products']
    context={"name":"E-commerce", "title":"checkout","form":form,"wishlist":wishlist ,
    "items":itemsordered,"totalitem":total}
    return render(request, "pages/checkout.html", context)


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

    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)
    context={"name":"Profile",'title':"E-COMMERCE","form":form,"wishlist":wishlist,"totalitem":total}
    return render(request, "pages/profile.html",context)




def rows(request):

    data= json.loads(request.body.decode('utf-8'));
    if data["load"] == "loaddetail":
        print(data["load"])
        rows = data["rows"];
        categoryrelatedid = data["cat"];
        sliceNo = int(data["slice"]);

        filteredrelated= Product.objects.all().filter(catigory=categoryrelatedid)

        rowstimescol= int(rows)*6 
        mydata=[]

        if len(Product.objects.all().filter(catigory=categoryrelatedid)) >= rowstimescol:
           
            
            filteredrelated=filteredrelated[:rowstimescol ];

            for product in filteredrelated:
                productjson={
                    'id':product.id,
                    'name':product.name,
                    'image':product.image.url,
                    'description':product.description,
                    'category':product.catigory.categoryName,
                    'old_price':product.old_price,
                    'new_price':product.new_price,
                    'owner':product.owner.username,
                    'rate':product.rate.rate,
                    'is_promotion':product.is_promotion}
                
                mydata.append(productjson)
            data_jsn={
                "data":mydata,
                "all":"no"
            }
        else:
            
            for product in filteredrelated:
                productjson={
                    'id':product.id,
                    'name':product.name,
                    'image':product.image.url,
                    'description':product.description,
                    'category':product.catigory.categoryName,
                    'old_price':product.old_price,
                    'new_price':product.new_price,
                    'owner':product.owner.username,
                    'rate':product.rate.rate,
                    'is_promotion':product.is_promotion}
                
                mydata.append(productjson)
            data_jsn={
                "data":mydata,
                "all":"yes"
            }
            
    elif data["load"] == "loadsearch":
        print(data["load"])
        rows = data["rows"];
        rowstoint= int(rows)*6;
        productsearchquery = data["query"];
        
        mydata=[]
        filteredrelated= getprodFiltered(productsearchquery,rowstoint)
        
        
        if len(filteredrelated["products"]) >= rowstoint:
            
      

            for product in filteredrelated["products"]:
                productjson={
                    'id':product.id,
                    'name':product.name,
                    'image':product.image.url,
                    'description':product.description,
                    'category':product.catigory.categoryName,
                    'old_price':product.old_price,
                    'new_price':product.new_price,
                    'owner':product.owner.username,
                    'rate':product.rate.rate,
                    'is_promotion':product.is_promotion}
                
                mydata.append(productjson)
            data_jsn={
                "data":mydata,
                "all":"no"
            }
            
            
        else:
            
            for product in filteredrelated["products"]:
                productjson={
                    'id':product.id,
                    'name':product.name,
                    'image':product.image.url,
                    'description':product.description,
                    'category':product.catigory.categoryName,
                    'old_price':product.old_price,
                    'new_price':product.new_price,
                    'owner':product.owner.username,
                    'rate':product.rate.rate,
                    'is_promotion':product.is_promotion}
                
                mydata.append(productjson)
            data_jsn={
                "data":mydata,
                "all":"yes"
            }
        
        
        


    return JsonResponse(data_jsn, safe=False)



class ProductDetailView(generic.DetailView):
    
    
    model=Product
    template_name="pages/detail.html"
    def get_context_data(self,**kwargs):

      
        total = super().get_context_data(**kwargs)
        products = super().get_context_data(**kwargs)
        
        total["relatedProducts"]= Product.objects.all().filter(catigory=self.object.catigory.pk)[:6]
        total["products"]=Product.objects.all()
        total["colors"]=Color.objects.all()
        total["sizes"]=Size.objects.all()
        total["totalitem"]=callcartnumber(self.request)['total']
        total["wishlist"]=callwishnumber(self.request)
        
        if self.request.user.is_authenticated:
            total["wishlists"]=Wishlist.objects.all().filter(customer=self.request.user)
            total['wishedproduct']=Wishlist.objects.all().filter(customer=self.request.user, product=self.object.pk)

            
        total['related']=Product.objects.all().filter(catigory=self.object.pk)

        try:
            total['wishedproduct']=total['wishedproduct'].first().product
        except:
            total['wishedproduct']=''

       
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

    total=callcartnumber(response)['total']
    wishlist=callwishnumber(response)
    context={"name":"E-commerce", "title":"New Product","form":form,"totalitem":total,"wishlist":wishlist}
    return render(response, "pages/AddProduct.html",context)

##my products 
@login_required
def myproducts(request):
    category=CategoryList.objects.all()
    data=Product.objects.all()
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)

    context={"name":"E-commerce", "title":"My Products","data":data,"totalprice":total,"wishlist":wishlist,"totalitem":total}
    
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
    
    if orderItem.quantity <= 0 or action == "removecartproduct":
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
            'is_promotion':product.is_promotion
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
    specialdeals= SpecialDeal.objects.all()
    sepcialarray=[]
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
            'is_promotion':hotdeal.product.is_promotion,
        }
       
        hotdealsarray.append(hotdealsobj)
        

    for spdeal in specialdeals:
        specialdealsobj={
            'id':spdeal.id,
            'originalproductid':spdeal.product.id,
            'name':spdeal.product.name,
            'image':spdeal.product.image.url,
            'description':spdeal.product.description,
            'category':spdeal.product.catigory.categoryName,
            'old_price':spdeal.product.old_price,
            'new_price':spdeal.product.new_price,
            'owner':spdeal.product.owner.username,
            'rate':spdeal.product.rate.rate,
            'is_promotion':spdeal.product.is_promotion,
        }
        sepcialarray.append(specialdealsobj)
        
    object_data1={
            'hotdeal':hotdealsarray,
            "specialdeal":sepcialarray
        }
    return JsonResponse(object_data1, safe=False)



# def ShippingApi(request):
#     category=CategoryList.objects.all()
#     data= json.loads(request.body)

  
#     items=OrderItem.objects.all()
#     ship=ShippingAddress.objects.all()
    
#     producthasbeenordered=[]
    
#     for item in items:
#         if request.user.is_authenticated:
#             if item.order.customer == request.user:
#                 itemname=item.product.name
#                 itemprice=item.product.new_price
#                 itemquantity=item.quantity
#                 proditem = {
#                     "product":itemname,
#                     "price":itemprice,
#                     "quantity":itemquantity
#                 }
#                 producthasbeenordered.append(proditem)

    


#     address=data["address"],
#     state=data["state"],
#     city=data["city"],
#     zipcode=data["zip"],
#     customer=request.user
#     #ordered=data["ordered"]

#     datapassed={
#         "address":data["address"],
#         "state":data["state"],
#         "city":data["city"],
#         "zip":data["zip"],
#         'email':data["email"],
#         "customer":request.user.username,
#         "customer email":request.user.email,
#         "ordered":producthasbeenordered
#     }

#     ##start our work excel

    

#     #end excel work

    
#     return JsonResponse(datapassed, safe=False)




def search(request):
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)

    searchData=SearchItem.objects.all() 
    try:
        q=request.GET.get("q")
    except:
        q=None
    
    if q:
        pagename="pages/search.html"
        query=q
    else:
        query=''
        pagename="pages/search.html"

    ip=get_client_ip(request)
    result= getprodFiltered(q,6)
    
    if request.user.is_authenticated:
        
        searchData, created = searchData.get_or_create(query=q, ip_addres=ip, user=request.user)
        searchData.save()
    else:
        searchData, created = searchData.get_or_create(query=q, ip_addres=ip, user=None)
        searchData.save()
    context={"query":query,"products":result["products"],
    "totalitem":total,"wishlist":wishlist}
    return render(request,"pages/search.html",context)


def category(request, category):
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)

    id_category_selected=CategoryList.objects.get(categoryName=category)
    result=Product.objects.all().filter(catigory=id_category_selected.id)
    
   
    context={"query":category,"products":result,
    "totalitem":total,"wishlist":wishlist}
    return render(request,"pages/category.html",context)


def brand(request, brand):
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)

    
    result=Product.objects.all().filter(brand_name=brand)
    
   
    context={"query":brand,"products":result,
    "totalitem":total,"wishlist":wishlist}
    return render(request,"pages/brand.html",context)



def listSearch(request):
        
    allproducts=Product.objects.all()
    productNames=[]
        
    for product in allproducts:
        productNames.append(product.name)
        # for clr in product.colors.all():
        #     print(clr)
        
    data_json ={
        "list" :productNames
    }

    return JsonResponse(data_json,safe=False)


def render_to_pdf(template_src, context_dic={}):
    template=get_template(template_src)
    html= template.render(context_dic)
    result=BytesIO()
    pdf= pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None



class ViewPdf(View):
    def get(self,request, *args , **kwargs):
        
        context_data={
            "name":request.user,
            "address":"mesdour",
            "email":request.user.email,
            "time":{
                "date":datetime.date.today(),
                
            },
            "data":shipDATA
        }
        template=get_template("pages/payement.html").render(context_data)
        pdf = render_to_pdf("pages/payement.html",context_data)
        # send_mail(

        #         "the subject",
        #         template,
        #         "moncefovi@yahoo.com",
        #         ["salemsifeddine1@gmail.com"],
        #         fail_silently=False
        # )
        msg=EmailMessage(
            "EZORA MARKET E-commerce Site",
            template,
            "moncefovi@yahoo.com",
            ["salemsifeddine1@gmail.com"],
            reply_to=["moncefovi@yahoo.com"]
         )
        
        msg.content_subtype= 'html'
        
        msg.send(fail_silently=False)

       
        return HttpResponse(pdf,content_type="application/pdf")




def data_fetch(request):
    ship=ShippingAddress.objects.all()
    ordered=OrderItem.objects.all()
    work = xlsxwriter.Workbook("data1.xlsx")
    work1 = xlsxwriter.Workbook("ordered.xlsx")
    sheet=work.add_worksheet()
    sheet1=work1.add_worksheet()

    sheet.write(f"A1","customer")
    sheet.write(f"B1","order")
    sheet.write(f"C1","email")
    sheet.write(f"D1","address")
    sheet.write(f"E1","city")
    sheet.write(f"F1","state")
    sheet.write(f"G1","zip1")
    sheet.write(f"H1","zip2")
    sheet.write(f"I1","date added")

    sheet1.write(f"A1","customer")
    sheet1.write(f"B1","order")
    sheet1.write(f"C1","product name")
    sheet1.write(f"D1","product price")
    sheet1.write(f"E1","quantity")
    sheet1.write(f"F1","total")
    sheet1.write(f"G1","ORDER")

    for ordrdn, ordrd in enumerate(ordered):
        # date_added
        sheet1.write(f"A{ordrdn + 2}",str(ordrd.order.customer.username))
        if ordrd.order.complete:
            sheet1.write(f"B{ordrdn + 2}","complete")
        else:
            sheet1.write(f"B{ordrdn + 2}","uncomplete")
        sheet1.write(f"C{ordrdn + 2}",str(ordrd.product.name))
        sheet1.write(f"D{ordrdn + 2}",str(ordrd.product.new_price))
        sheet1.write(f"E{ordrdn + 2}",str(ordrd.quantity))
        sheet1.write(f"F{ordrdn + 2}",str(ordrd.quantity * ordrd.product.new_price))
        sheet1.write(f"G{ordrdn + 2}",str(ordrd.order))

    for idk, shi in enumerate(ship):
        # date_added
       
        sheet.write(f"A{idk + 2}",str(shi.customer))
        sheet.write(f"B{idk + 2}",str(shi.order))
        sheet.write(f"C{idk + 2}",str(shi.email))
        sheet.write(f"D{idk + 2}",shi.address)
        sheet.write(f"E{idk + 2}",shi.city)
        sheet.write(f"F{idk + 2}",shi.state)
        sheet.write(f"G{idk + 2}",str(shi.zip_code1))
        sheet.write(f"H{idk + 2}",str(shi.zip_code2))
        sheet.write(f"I{idk + 2}",str(shi.date_added))

    work.close()
    work1.close()

    return render(request, "pages/profile.html",{})


def wishlistApi(request):
    data= json.loads(request.body.decode('utf-8'))
    idproduct= data["productId"]
    action= data["action"]

    product_wished= Product.objects.all().filter(id=idproduct)
   
        
   
    if action == "add":
        wish , created = Wishlist.objects.get_or_create(customer=request.user, product=product_wished.first())
        wish.save()
    elif action == "removewish":
        wish= Wishlist.objects.get(customer=request.user, product=product_wished.first()).delete() 
        
    
    data_json={}
    return JsonResponse( data_json, safe=False)


def wishlist(request):
    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)
    
    if request.user.is_authenticated:
        wishlists=Wishlist.objects.all().filter(customer=request.user)
    else:
        wishlists=[]
   
    
    
    
    context={"wishlists":wishlists,"wishlist":wishlist,"totalitem":total}

    return render(request, "pages/wishlist.html", context)




def deal(request, deal):

    total=callcartnumber(request)['total']
    wishlist=callwishnumber(request)

    
    product=Product.objects.all().filter(name=deal)
    
   
    context={"product":product.first(),
    "totalitem":total,"wishlist":wishlist}

    return render(request, "pages/deal.html",context)

