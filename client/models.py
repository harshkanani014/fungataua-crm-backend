from django.db import models
from datetime import date
# Create your models here.

class Status(models.Model):
    status = models.TextField(max_length=1000, unique=True)

    def __str__(self):
        return self.status

class Client(models.Model):
    first_name = models.TextField(max_length=1000)
    last_name = models.TextField(max_length=1000) 
    email = models.EmailField()
    date_of_birth = models.DateField()
    phone_number = models.TextField(max_length=20)
    gender = models.TextField(max_length=20)
    address = models.TextField(max_length=10000) 
    state = models.TextField(max_length=1000)
    city = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="client_images/")
    
    def __str__(self):
        return self.email


class Services(models.Model):
    service_name = models.TextField(max_length=1000, unique=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name


class SubCategory(models.Model):
    subcategory_name = models.TextField(max_length=1000, unique=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.subcategory_name


class Category(models.Model):
    category_name = models.TextField(max_length=1000)
    is_enabled = models.BooleanField(default=True)
    subcategory = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)    

    def __str__(self):
        return self.category_name 


# The below table is the table for many to many relationship between client entity and service entity
class client_service_records(models.Model):
    date_of_visit = models.DateField(default=date.today())
    email = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    services = models.ForeignKey(to=Services, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE, default=0)
    remarks = models.TextField(max_length=10000, default="")
   

     