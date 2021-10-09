from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Rate)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(CategoryList)
admin.site.register(Hotdeals)
admin.site.register(SpecialDeal)
admin.site.register(AdBanner)
admin.site.register(Slider)
admin.site.register(HorAdd)
admin.site.register(NewsLetterEmails)

admin.site.register(SearchItem)
