"""
URL configuration for ttt project.

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
from django.contrib import admin
from django.urls import path
from myapp.views import CartView
from myapp.views import ProductTagsView
from myapp.views import FavoriteProductsView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart')
    path('product/<int:product_id>/tags/', ProductTagsView.as_view(), name='product_tags'),
    path('user/<int:user_id>/favorites/', FavoriteProductsView.as_view(), name='user_favorites'),
]
