from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cate_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)



