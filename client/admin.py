from django.contrib import admin
from .models import Status, Client, Services, SubCategory, Category, client_service_records
# Register your models here.
admin.site.register(Status)
admin.site.register(Client)
admin.site.register(Services)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(client_service_records)
