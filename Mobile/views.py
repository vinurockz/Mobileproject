from django.shortcuts import render,redirect
from django.views.generic import TemplateView



from .models import Brand_Field,Mobile_Details,Orders

from .forms import Brand_Create_Form,Mobile_Create_Form,Mobile_Update_Form


def Main_page(req):
    return render(req, "index.html")

def HomePage(req):
    return render(req,"main.html")


class MobilCreateView(TemplateView):
    model=Mobile_Details
    form_class=Mobile_Create_Form
    template_name = "mobilcreate.html"
    context={}

    def get(self,req,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(req,self.template_name,self.context)
    def post(self,req,*args,**kwargs):
        form=self.form_class(req.POST,files=req.FILES)
        if form.is_valid():
            form.save()
            return render(req,self.template_name,self.context)

class MobilListView(TemplateView):
    template_name = "listmob.html"
    context={}
    model=Mobile_Details

    def get(self,req,*args,**kwargs):
        listed = Mobile_Details.objects.all()
        self.context["lists"] = listed
        return render(req,self.template_name,self.context)

class MobileUpdatView(TemplateView):
    template_name = "updatemob.html"
    model=Mobile_Details
    form_class=Mobile_Update_Form
    context={}
    def get(self,req,*args,**kwargs):
        id = kwargs.get("pk")
        mobile = self.model.objects.get(id=id)
        form = self.form_class(instance=mobile)
        self.context["form"]=form
        return render(req,self.template_name,self.context)

    def post(self,req,*args,**kwargs):
        id = kwargs.get("id")
        mobile=self.model.objects.get(id=id)
        form=self.form_class(req.POST,files=req.FILES,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("listed")

class MobileDeleteView(TemplateView):
    model=Mobile_Details

    def get(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        mobile=self.model.objects.get(id=id)
        mobile.delete()
        return redirect("listed")

class MobileDetail(TemplateView):
    model=Mobile_Details
    template_name = "itemDetail.html"
    context={}
    def get(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        itemlist=self.model.objects.get(id=id)
        self.context["items"]=itemlist
        return render(req,self.template_name,self.context)

class ViewOrders(TemplateView):
    def get(self,req,*args,**kwargs):
        orders=Orders.objects.exclude(status="cancelled")
        context={
            "orders":orders
        }
        return render(req,"buyorders.html",context)



