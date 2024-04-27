from django.contrib.auth.models import User
from django.db import models


class ProductImage(models.Model):
    image = models.ImageField(upload_to='img/')


class Product(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    data_create = models.DateField(auto_now_add=True)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default='editor')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=30, default='user')
