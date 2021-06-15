from django.db import models

# Create your models here.
class Brand_Field(models.Model):
    brand_name=models.CharField(max_length=80)

    def __str__(self):
        return self.brand_name

class Mobile_Details(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand_name=models.ForeignKey(Brand_Field,on_delete=models.CASCADE)
    spec=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.mobile_name

class Carts(models.Model):
    product=models.ForeignKey(Mobile_Details,on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    options = (("cart", "cart"),
          ("orderplaced", "orderplaced"))
    status = models.CharField(max_length=120,choices=options,default="cart")


    def __str__(self):
        return self.product

class Orders(models.Model):
    product=models.ForeignKey(Mobile_Details,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    date=models.DateField(auto_now=True)
    address=models.CharField(max_length=200)
    options=(("ordered","ordered"),("packed","packed"),("shipped","shipped"),
             ("delivered","delivered"),("cancelled","cancelled"))
    status=models.CharField(max_length=120,choices=options,default="ordered")