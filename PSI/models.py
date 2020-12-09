from django.db import models
from django.contrib.auth.models import User
import datetime

LISTED_CHOICES = [
    ('y', 'Yes'),
    ('n', 'No'),
]

class Customer(models.Model):
    user = models. OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True, )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    css = models.FloatField(default=0,null=False)

    def __str__(self):
        return self.name

    @property
    def get_css(self):
        return self.css

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    pss = models.FloatField(default=0,null=True, blank=True)
    listed = models.CharField(default='n',max_length=1, choices=LISTED_CHOICES)
    packaging_name = models.CharField(max_length=200,null=True)
    carbon_footprint = models.FloatField(default=0, null=True, blank=True)
    biodegradability = models.FloatField( default=0, null=True, blank=True)
    recyclability = models.FloatField(default=0, null=True, blank=True)
    energy = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

"""
class Unprocessed_item(models.Model):
    name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.name
"""


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True, auto_now=False)
    complete = models.BooleanField(default=False ,null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    Average_PSS = models.FloatField(default=0, null=True, blank=True)
    used = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def shipping(self):
        shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_PSS(self):
        orderitems = self.orderitem_set.all()
        try:
            A = sum([item.get_totalPSS for item in orderitems])
            B = len(orderitems)
            total = A / B
        except:
            total = 0
        return total

    @property
    def get_cust_CSS(self):
        return self.customer.css



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_totalPSS(self):
        total = self.product.pss
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
















# Create your models here.

