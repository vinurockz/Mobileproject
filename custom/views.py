from django.shortcuts import render,redirect
from .forms import UserCreaForm,Loginform,OrederForm,BuyOrder
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Mobile.models import Mobile_Details,Carts,Orders



class UserReg(TemplateView):
    model=User
    form_class=UserCreaForm
    template_name = "regis.html"
    context={}
    def get(self,req,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(req,self.template_name,self.context)

    def post(self,req,*args,**kwargs):
        form=self.form_class(req.POST)
        if form.is_valid():
            form.save()
            return redirect("loged")
        else:
            return redirect("regised")

def Main_pages(req):
    return render(req, "mains.html")


class Login(TemplateView):
    form_class=Loginform
    model=User
    context={}
    template_name = "login.html"

    def get(self,req,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(req,self.template_name,self.context)
    def post(self,req,*args,**kwargs):
        v="login Failed "
        form=self.form_class(req.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(req,username=username,password=password)
            if(user):
                login(req,user)
                return redirect("ordered")
            else:
                return redirect("loged")


class indexview(TemplateView):
    template_name ="order.html"
    context={}

    def get(self,req,*args,**kwargs):
        mobile=Mobile_Details.objects.all()
        self.context["mobiles"]=mobile
        return render(req,self.template_name,self.context)



class MyCart(TemplateView):
    model=Carts
    template_name = "mycart.html"
    context={}


    def get(self,req,*args,**kwargs):
        mycart=self.model.objects.filter(user=req.user,status="cart")

        self.context["item"]=mycart
        return render(req,self.template_name,self.context)


class AddtoCart(TemplateView):
    model=Carts
    def get(self,req,*args,**kwargs):
        pid=kwargs.get("id")
        mobile=Mobile_Details.objects.get(id=pid)
        user=req.user
        cart=Carts(product=mobile,user=user)
        cart.save()
        return redirect("carted")




class RemoveCart(TemplateView):
    model=Carts
    def get(self,req,*args,**kwargs):
        id=kwargs.get("id")
        carts=self.model.objects.get(id=id)
        carts.delete()
        return redirect("carted")






def oderders(req):
    return render(req,"mobiledetailes.html")


class Placeorder(TemplateView):
    model=Orders
    form_class = OrederForm
    template_name = "place.html"
    context={}
    def get_object(self,id):
        return Mobile_Details.objects.get(id=id)
    def get(self,req,*args,**kwargs):
        pid=kwargs.get("id")
        mobile=self.get_object(pid)
        mycart = Carts.objects.filter(product=mobile,user=req.user)
        for cart in mycart:
            cart.status="oderplaced"
            cart.save()
            print("oderplaced")
        form=self.form_class(initial={"product":mobile.mobile_name})
        self.context["form"]=form
        return render(req,self.template_name,self.context)
    def post(self,req,*args,**kwargs):
        pid=kwargs.get("id")
        mobile=self.get_object(pid)
        address=req.POST.get("address")
        user = req.user
        product = mobile
        myorder = self.model(product=product, user=user, address=address)
        myorder.save()
        return redirect("indexed")

class ViewOrder(TemplateView):

    def get(self,req,*args,**kwargs):
        orders = Orders.objects.filter(user=req.user)
        context={
            "orders" : orders
        }
        return render(req,"buyorder.html",context)






class CancellOrder(TemplateView):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("id")
        order=Orders.objects.get(id=id)
        order.status="cancelled"
        order.save()
        return redirect("buyed")

def Logout_page(req):
    logout(req)
    return redirect("loged")
