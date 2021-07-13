from django.db import models
from django.contrib.auth.models import AbstractUser


# Admin/superAdmin database model
class User(AbstractUser):
    name = models.TextField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=1000)
    client_add = models.BooleanField(default=False)
    client_edit = models.BooleanField(default=False)
    services_add = models.BooleanField(default=False)
    services_edit = models.BooleanField(default=False)
    category_add = models.BooleanField(default=False)
    category_edit = models.BooleanField(default=False)
    status_add = models.BooleanField(default=False)
    status_edit = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# model for saving otp of user and its expiry
class loginDetails(models.Model):

    email = models.EmailField(unique=True)
    otp = models.TextField()
    exp = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.email