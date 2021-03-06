from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    # 'on_delete=models.CASCADE' delets the user related to customer when the customer is deleted
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = 'default_profile.png', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        if(self.name == None):
            return 'Unknown user'
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, choices = CATEGORY, null = True)
    description = models.CharField(max_length = 300, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    # a product can have multiple tags as well as a tag can be related to multiple products
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    def __str__(self):
        return self.product.name

    # a customer can have many orders but the vice versa is not true
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    # a product can be related to many orders but the vice versa is not true
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 200, choices = STATUS, null = True)