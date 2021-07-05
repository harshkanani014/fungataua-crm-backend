from django.urls import path
from .views import *

urlpatterns = [
      path('add-status/', AddStatus.as_view()),
      path('edit-status/<status>', EditStatus.as_view()),
      path('get-status/', GetStatus.as_view())
 ]