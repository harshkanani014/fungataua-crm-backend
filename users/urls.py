from django.urls import path
from .views import *

urlpatterns = [
    path('edit-user/<email>', EditUser.as_view()),
    path('add-user', AddUserView.as_view()),
    path('get-user', GetUser.as_view())
]