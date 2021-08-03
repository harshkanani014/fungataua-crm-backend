from accounts.models import User
from django.db import models
from datetime import date


# Model for status
class Status(models.Model):
    status = models.TextField(max_length=1000, unique=True)

    def __str__(self):
        return self.status


# Model for client basic details
class Client(models.Model):
    first_name = models.TextField(max_length=1000)
    last_name = models.TextField(max_length=1000) 
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone_number = models.TextField(max_length=20)
    gender = models.TextField(max_length=20)
    address = models.TextField(max_length=10000) 
    city = models.TextField(max_length=1000)
    ethinicity = models.TextField(max_length=1000)
    emergency_phone_number = models.TextField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.email


# Model for client documents images
class Client_images(models.Model):
    date_of_add = models.DateField(default=date.today()) 
    email = models.ForeignKey(to=Client, on_delete=models.CASCADE)   # FK
    image = models.FileField(upload_to="client_images")
    image_name = models.TextField(null=True)


# Model for services
class Services(models.Model):
    service_name = models.TextField(max_length=1000, unique=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name


# Model for SubCategory
class SubCategory(models.Model):
    subcategory_name = models.TextField(max_length=1000, unique=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.subcategory_name


# Model for category
class Category(models.Model):
    category_name = models.TextField(max_length=1000)
    is_enabled = models.BooleanField(default=True)
    subcategory = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)    

    def __str__(self):
        return self.category_name 


# Model for Client Service Records
class client_service_records(models.Model):
    date_of_visit = models.DateField(default=date.today()) 
    added_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    email = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    services = models.ForeignKey(to=Services, on_delete=models.CASCADE)
    refered_by = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(to=Status, on_delete=models.CASCADE)
    remarks = models.TextField(max_length=10000)