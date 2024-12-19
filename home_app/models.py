from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    colors = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)

    def __str__(self):
        return self.name


class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    total_price = models.IntegerField(default=0)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    product_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('color', 'size', 'product_name', 'username')

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    subj = models.CharField(max_length=30)
    msg = models.TextField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

