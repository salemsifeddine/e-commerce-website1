from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest, request
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
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout,name="logout"),
    path("profil/",views.profil, name="profil"),
    path(r"product/<int:pk>/",views.ProductDetailView.as_view(),name="detail"),
    path("product/new/", views.addproduct, name="newproduct"),
    path("product/myProducts/",views.myproducts, name="myproducts"),
    path("update/", views.UpdateItem),
    path("updateproducts/", views.UpdateProducts),
    path("hotdeals/", views.HotdealsApi),
    path("adapi/", views.adsapi),
    # path("shipping/",views.ShippingApi, name="shipping"),
    path("shipping/",views.data_fetch, name="shipping"),
    path("category/<str:category>",views.category, name="category"),
    path("brand/<str:brand>",views.brand, name="brand"),
    path("apilistSearch/", views.listSearch),
    path("checkout/payement/", views.ViewPdf.as_view(), name="payement-pdf"),
    path("wishlistApi/", views.wishlistApi, name="wishlistApi"),
    path("rows/", views.rows),
    path("deals/<str:deal>/", views.deal, name="deal"),
    path("wishlist/", views.wishlist, name="wishlist"),
    
    
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



 


SOCIAL_AUTH_URL_NAMESPACE = "users:social"