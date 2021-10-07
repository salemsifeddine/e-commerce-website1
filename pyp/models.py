from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import math
# Create your models here.

#class Customer(models.Model):
#    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#    name=models.CharField(max_length=200, null=True)
#    
#    def __str__(self):
#        return self.name
        
class CategoryList(models.Model):
    categoryName= models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.categoryName

class Rate(models.Model):
    rate= models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.rate}"
    
class Product(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=150)
    old_price=models.FloatField()
    new_price= models.FloatField()
    catigory=models.ForeignKey(CategoryList, on_delete=models.CASCADE, default=1)
    rate=models.ForeignKey(Rate, on_delete=models.CASCADE, default=0)
    image= models.ImageField( default="products/defaultProduct.jpg", upload_to="products")

    #date_added=models.DateTimeField(auto_now_add=True)
    #def save(self, *args, **kwargs):
    #    super().save(*args,**kwargs)
    #    img = Image.open(self.image.path)
    #    width=math.floor(img.width/1.5)
    #    height=math.floor(img.height/1.5)
    #    new_size = (height,width)
    #    img = img.resize(new_size, Image.ANTIALIAS)
    #    img.save(self.image.path)

    
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_order= models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
        
   # @property
   # def totalProducts(self):
   #     item=self.objects.orderItem_set()
   #     totalarray = [quantnumnber.quantity for quantnumnber in item]
   #     total = sum(totalarray)
   #     return total


class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, db_constraint=False)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL,default=0 ,null=True, db_constraint=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total= self.product.new_price * self.quantity
        return total
    

class ShippingAddress(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address=models.CharField(max_length=200, null = False)
    city= models.CharField(max_length=200, null=False)
    state=models.CharField(max_length=200, null=False)
    zip_code=models.CharField(max_length=200, null=False)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
        

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField( default="Users/default.jpg", upload_to="Users")
    def __str__(self):
        return f"{self.user.username} profile"

    #def save(self, *args, **kwargs):
    #    super().save(*args,**kwargs)
    #    img = Image.open(self.image.path)
    #    width=math.floor(img.width/1.5)
    #    height=math.floor(img.height/1.5)
    #    new_size = (height,width)
    #    img = img.resize(new_size, Image.ANTIALIAS)
    #    img.save(self.image.path)

class Hotdeals(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=False)
    date_added=models.DateTimeField(auto_now_add=True)

class SpecialDeal(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=False)
    date_added=models.DateTimeField(auto_now_add=True)

class AdBanner(models.Model):
    image=models.ImageField(blank=True,upload_to="adImagesBnner")
    video=models.FileField(blank=True,upload_to="adVediosBanner")

class Slider(models.Model):
    image=models.ImageField(blank=True,upload_to="slideImages")
    video=models.FileField(blank=True,upload_to="slideVideos")
    button=models.CharField(blank=True,max_length=10)
    urlbutton=models.TextField(blank=True)

class HorAdd(models.Model):
    image=models.ImageField(blank=True,upload_to="HorAdImages")
    video=models.FileField(blank=True,upload_to="HorAdsHorAdImages")

class NewsLetterEmails(models.Model):
    email=models.EmailField(blank=False)
    
    def __str__(self):
        return self.email