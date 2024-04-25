from django.db import models

# Create your models here.

class Student(models.Model):
    #id= models.AutoField()
    name = models.CharField(max_length=100)
    age =models.IntegerField()
    email = models,models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models,models.FileField()
    
 
 
class Product(models.Model):
    pass