from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Catigory)
admin.site.register(Rate)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
