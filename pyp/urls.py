from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as view


urlpatterns = [
    path("",views.main,name="home"),
    path("cart/", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("login/",view.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout,name="logout"),
    path("profil",views.profil, name="profil"),
    path(r"product/<int:pk>/",views.ProductDetailView.as_view(),name="detail"),
    path("product/new/", views.addproduct, name="newproduct"),
    path("product/myProducts/",views.myproducts, name="myproducts"),
    path("update/", views.UpdateItem, name="update"),
    path("shipping/",views.ShippingApi, name="shipping"),
    
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)