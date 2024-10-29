"""
URL configuration for merch_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import index,my_search,product_detail,blog,blog_detail,product_comment,product_list_by_category,qaview,cart,add_to_cart,shopping

app_name = 'app_market'

urlpatterns = [
    path('',index,name='home'),
    path('search/', my_search, name='search'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/<int:id>/comment/', product_comment, name='p_comment'),
    path('blog/', blog , name='blog' ),
    path('blog/detail/', blog_detail , name='blogdetail' ),
    path('products/category/<int:category_id>/', product_list_by_category, name='product_list_by_category'),
    path('qa/', qaview , name='qa' ),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'), 
    path('cart/1', shopping, name='shopping'),   
] 
