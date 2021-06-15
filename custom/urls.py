from django.urls import path
from .views import UserReg,Login,indexview,MyCart,AddtoCart,RemoveCart,oderders,Placeorder,ViewOrder,CancellOrder,Main_pages,Logout_page


urlpatterns = [
    path("regis",UserReg.as_view(),name="regised"),
    path("log",Login.as_view(),name="loged"),
    path("index",oderders,name="indexed"),
    path("cart",MyCart.as_view(),name="carted"),
    path("addcart/<int:id>",AddtoCart.as_view(),name="addcarted"),
    path("rmcart/<int:id>",RemoveCart.as_view(),name="rmcarted"),
    path("order",indexview.as_view(),name="ordered"),
    path("place/<int:id>",Placeorder.as_view(),name="placed"),
    path("buy",ViewOrder.as_view(),name="buyed"),
    path("main",Main_pages,name="mained"),
    path("cancell/<int:id>",CancellOrder.as_view(),name="cancelled"),
    path("logout",Logout_page,name="logout")
]
