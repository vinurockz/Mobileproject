"""MobileShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import MobilCreateView,Main_page,HomePage,MobilListView,MobileUpdatView,MobileDeleteView,MobileDetail,ViewOrders

urlpatterns = [
    path("create",MobilCreateView.as_view(),name="created"),
    path("",HomePage,name="maines"),
    path("home",Main_page,name="homed"),
    path("list",MobilListView.as_view(),name="listed"),
    path("edit/<int:pk>",MobileUpdatView.as_view(),name="edited"),
    path("delete/<int:pk>",MobileDeleteView.as_view(),name="deleted"),
    path("detail/<int:pk>",MobileDetail.as_view(),name="detailed"),
    path("view",ViewOrders.as_view(),name="viewed")
]
