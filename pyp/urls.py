from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("",views.main,name="home"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("login/",view.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout,name="logout"),
    path("profil/",views.profil, name="profil"),
    path(r"product/<int:pk>/",views.ProductDetailView.as_view(),name="detail"),
    path("product/new/", views.addproduct, name="newproduct"),
    path("product/myProducts/",views.myproducts, name="myproducts"),
    path("update/", views.UpdateItem),
    path("updateproducts/", views.UpdateProducts),
    path("hotdeals/", views.HotdealsApi),
    path("adapi/", views.adsapi),
    path("shipping/",views.ShippingApi, name="shipping"),
    path("products/<str:category>",views.category, name="category"),
    path("apilistSearch/", views.listSearch),
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)