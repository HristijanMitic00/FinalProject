from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    processed = models.BooleanField(default=False, null=True)
    transaction_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total_from_cart(self):
        orderedkits = self.orderedproduct_set.all()
        total = sum([kit.get_total for kit in orderedkits])
        return total
    
    @property
    def get_kit_from_cart(self):
        orderedkits = self.orderedproduct_set.all()
        total = sum([kit.quantity for kit in orderedkits])
        return total
    
class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_cart = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingProduct(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
     address = models.CharField(max_length=100)
     city = models.CharField(max_length=100)
     country = models.CharField(max_length=100)
     zipcode = models.CharField(max_length=100)
     date_shipped = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.address




    