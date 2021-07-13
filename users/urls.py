from django.urls import path
from .views import *


urlpatterns = [
    # User API endpoints
    path('edit-user/<int:id>', EditUser.as_view()),

    path('add-user', AddUserView.as_view()),

    path('get-user', GetUser.as_view())
]