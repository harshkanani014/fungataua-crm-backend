from django.urls import path
from .views import *

urlpatterns = [
      path('add-status/', AddStatus.as_view()),
      path('edit-status/<status>', EditStatus.as_view()),
      path('get-status/', GetStatus.as_view()),
      path('add-service/', AddService.as_view()),
      path('edit-service/<service_name>', EditService.as_view()),
      path('get-service/', GetService.as_view()),

 ]